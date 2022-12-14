import random
import os
import sys


def markov_lib(key, character1):
    data_sample = "moby-dick.txt"
    text_data = open(data_sample, 'r').read()
    text_data = ''.join([i for i in text_data if not i.isdigit()]).replace("\n", " ").split(' ')
    markov_lib = {}

    for i in range(len(text_data)-key):
        word = " ".join(text_data[i:i+key])
        if word.lower() in markov_lib.keys():
            markov_lib[word.lower()].append(text_data[i+key])
        else:
            markov_lib[word.lower()] = [text_data[i+key]]

    try:
        character2 = random.choice(markov_lib[character1.lower()])
    except KeyError as e:
        return ("fail")
    return character2

def keyboard():
    key = int(input("Choose your accuracy level: "))
    first_word = input("Input your first word: ")
    message = first_word
    while(True):
        os.system('cls')
        first_word = " ".join(message.split()[0-key:])
        predicted_next_word = markov_lib(key,first_word)
        if predicted_next_word == "fail":
            print("-------------------------\nThe training text is not big enough to predict the next word. Exited")
        response = input(message +" ["+predicted_next_word+"] ")

        if response == "t" or response == "T":
            #os.system('cls')
            message = message + " " + predicted_next_word
        if response == "f" or response == "F":
            os.system('cls')
            response = input(message + " ")
            message = message + " " +response

        if response == "E" or response == "e":
            print(message)
            break

def text_generator():
    choice = input("Choose the functionality: \n 1 - Make a sentence\n 2 - Generate a paragraph with chosen number of words \n Your choice: ")
    key = int(input("Choose your accuracy level: "))
    character1 = input("Input your first word: ")
    if choice == "1":
        sentence_stopper = ['.', '?', '!']
        message = character1.capitalize()
        while message[-1] not in sentence_stopper:
            try:
                character2 = markov_lib(key,character1)
                message += " " + character2
                character1 = " ".join((message.split())[-(key):])
            except KeyError as e:
                print("-------------------------\nThe training text is not big enough to generate the next word. Exited")
        print (message)

    if choice == "2":
        word_count = int(input("The number of words want to be generated: "))
        message = character1.capitalize()
        for i in range(word_count):
            try:
                character2 = markov_lib(key,character1)
                message += " " + character2
                character1 = " ".join((message.split())[-(key):])
            except KeyError as e:
                print("-------------------------\nThe training text is not big enough to generate the next word. Exited")
        print(message)

def main_run():
    choice = input("Hey there, welcome to our program\n Please choose the functionality :> \n 1 - Keyboard prediction \n 2- Paragraph generator \n Your choice: ")
    if choice == "1":
        keyboard()
    if choice == "2":
        text_generator()

main_run()
