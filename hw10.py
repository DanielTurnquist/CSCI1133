def scrabble_score(word):
    # ==========================================
    # Purpose: determines the scrabble score of a given word
    # Input Parameter(s): word - a string representing the word
    # Return Value(s): an integer representing the word's scrabble score
    # ==========================================
    scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
              'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
              'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1,
              't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    if len(word) == 0:
        return 0
    return scores[word[0]] + scrabble_score(word[1:])

def relatively_prime(x,y):
    # ==========================================
    # Purpose: checks whether two integers are relatively prime
    # Input Parameter(s):
    # x - the first integer
    # y - the second integer
    # Return Value(s): a Boolean representing whether the two integers are relatively prime
    # ==========================================
    return gcd(x,y) == 1

def gcd(x, y, divisor = 0, initializer = True):
    # ==========================================
    # Purpose: finds the greatest common divisor of two integers
    # Input Parameter(s):
    # x - the first integer
    # y - the second integer
    # divisor - the number being checked as a possible greatest common divisor
    # initializer - a Boolean representing whether this instance of the function is the initial call
    # Return Value(s): an integer representing the greatest common divisor
    # ==========================================
    if initializer:
        divisor = min(x, y)
    if x % divisor == 0 and y % divisor == 0:
        return divisor
    else:
        return gcd(x, y, divisor - 1, False)

def find_filepath(directory, filename):
    # ==========================================
    # Purpose: finds a file in a directory and its path there, or indicates that the file isn't present
    # Input Parameter(s): directory - the directory in which the file should be contained (string)
    # filename - the name of the file (string)
    # Return Value(s): a string representing the file path, or a Boolean False indicating that the file is not in the directory
    # ==========================================
    if filename in directory:
        return f'{directory[0]}/{filename}'
    else:
        for ele in directory:
            if type(ele) == list:
                x = find_filepath(ele, filename)
                if type(x) == str:
                    return f'{directory[0]}/' + x
    return False




