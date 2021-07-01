import random

def combine(d1, d2):
    #==========================================
    # Purpose: Combines 2 dictionaries into one with all keys and values, and added values if a key is present in both
    # Input Parameter(s):
    # d1 - the first dictionary
    # d2 - the second dictionary
    # Return Value(s):
    # A combined dictionary
    #==========================================
    dsum = {}
    for key in d1:
        dsum[key] = d1[key]
    for key in d2:
        if key not in dsum:
            dsum[key] = d2[key]
        elif key in dsum:
            dsum[key] += d2[key]
    return dsum

def first_words(fname):
    # ==========================================
    # Purpose: returns a dictionary containing all of the first words (and how often they appear) of sentences contained within a file
    # Input Parameter(s): fname - the name of the file (string)
    # Return Value(s): a dictionary containing strings of the first words as keys and the number of occurrences as values
    # ==========================================
    output = {}
    with open(fname, 'r') as txtfile:
        for line in txtfile:
            first_word = line.split(' ')[0]
            if first_word not in output:
                output[first_word] = 1
            else:
                output[first_word] += 1
    return output

def next_words(fname):
    # ==========================================
    # Purpose: returns a dictionary with the words in a file other than the first word of each sentence and their occurrences
    # Input Parameter(s): fname - the name of the file (string)
    # Return Value(s): a dictionary with the words other than the first word of each sentence as keys and their frequencies as values
    # ==========================================
    output = {}
    word_list = []
    with open(fname, 'r') as txtfile:
        for line in txtfile:
            line_list = line.strip().split(' ')
            for i in range(len(line_list)):
                if line_list[i] != '.':
                    if line_list[i] not in output:
                        output[line_list[i]] = {}
            word_list += line_list
        for i in range(len(word_list))[1::]:
            word = word_list[i]
            previous_word = word_list[i-1]
            if previous_word != '.':
                if word not in output[previous_word]:
                    output[previous_word][word] = 1
                elif word in output[previous_word]:
                    output[previous_word][word] += 1
    return output

def fanfic(fname):
    # ==========================================
    # Purpose: takes in a file and randomly writes a new one based on its contents
    # Input Parameter(s): fname - the name of the file (string)
    # Return Value(s): None
    # ==========================================
    initial_words = first_words(fname)
    following_words = next_words(fname)
    for i in range(10):
        word = random.choice(list(initial_words))
        sentence = ''
        while word != '.':
            sentence += ' ' + word
            word = random.choice(list(following_words[word]))
        print(sentence + ' .')


































