import random
def markov_text():
    data_sample = "moby-dick.txt"
    text_data = open(data_sample, 'r').read()
    text_data = ''.join([i for i in text_data if not i.isdigit()]).replace("\n", " ").split(' ')
    index = 1
    markov_gen = {}
    word_count = int(input('select the number of words you want to generate')) #need to connect this with input box

    for character in text_data[index:]:
            key = text_data[index-1]
            if key in markov_gen:
                markov_gen[key].append(character)
            else:
                markov_gen[key] = [character]
            index += 1
    
            character1 = random.choice(list(markov_gen.keys()))
            message = character1.capitalize()
            

            while len(message.split(' ')) < word_count:
                character2 = random.choice(markov_gen[character1])
                character1 = character2
                message += ' ' + character2
            return message

markov_text