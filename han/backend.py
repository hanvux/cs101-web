import random
import os
import sys
from js import document
from pyodide import create_proxy

def _mode_change(*args, **kwargs):
    choice = document.getElementById("choices").value
    if choice == 'one':
        document.getElementById("number").disabled = True
    else:
        document.getElementById("number").disabled = False
mode_change = create_proxy(_mode_change)
document.getElementById("choices").addEventListener("input", mode_change)

def _text_generator(*args, **kwargs):
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

    choice = document.getElementById("choices").value
    acc = document.getElementById("accuracy").value
    key = int(acc)

    character1 = document.getElementById("word").value

    number = document.getElementById("number").value
    word_count = int(number)

    if choice == "one":
        sentence_stopper = ['.', '?', '!']
        message = character1.capitalize()
        while message[-1] not in sentence_stopper:
            try:
                character2 = markov_lib(key,character1)
                message += " " + character2
                character1 = " ".join((message.split())[-(key):])
            except KeyError as e:
                document.getElementById("output").innerText = "The training text is not big enough to generate the next word. Exited"
        document.getElementById("output").innerText = f"The result is: {message}"

    else:
        message = character1.capitalize()
        for i in range(word_count):
            try:
                character2 = markov_lib(key,character1)
                message += " " + character2
                character1 = " ".join((message.split())[-(key):])
            except KeyError as e:
                document.getElementById("output").innerText="-------------------------\nThe training text is not big enough to generate the next word. Exited"
        document.getElementById("output").innerText = f"The result is: {message}"

text_generator = create_proxy(_text_generator)
document.getElementById("result-btn").addEventListener("click", text_generator)

_mode_change()
