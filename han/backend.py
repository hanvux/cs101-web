
import js
from js import document
import random
import os
import sys

one_keyboard = Element("1-keyboard")
two_para = Element("2-para")

t = Element("continue")
f = Element("noo")

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
    key = Element('quantity').element.value
    first_word = Element('input-word').element.value
    message = first_word
    while(True):
        os.system('cls')
        first_word = " ".join(message.split()[0-key:])
        predicted_next_word = markov_lib(key,first_word)
        if predicted_next_word == "fail":
            print("-------------------------\nThe training text is not big enough to predict the next word. Exited")
            sys.exit(1)
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
                return (message)
        return (message)

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
                return(message)
        return(message)


def para():
    print(text_generator())
