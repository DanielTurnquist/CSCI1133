# Exam 3
# Daniel Turnquist

# Problem A:
# Recursion

def count_big(num_lst, tally = 0):
    if len(num_lst) == 0:
        return tally
    if num_lst[0] > 99:
        return count_big(num_lst[1:], tally + 1)
    return count_big(num_lst[1:], tally)

def two_big(lst_lst, counter = 0):
    if len(lst_lst) == 0:
        return counter
    counter += count_big(lst_lst[0])
    return two_big(lst_lst[1:], counter)


# Problem B:
# Dictionaries

def to_indexes(string):
    out = {}
    for ch in string:
        out[ch] = []
    for i in range(len(string)):
        out[string[i]] += [i]
    return out


# Problem C:
# Objects

class Lake:
    def __init__(self, name, area, depth):
        self.name = name
        self.area = area
        self.depth = depth
    def __str__(self):
        return f'{self.name} - Area: {self.area}, Depth: {self.depth}'
    def __lt__(self, other):
        return self.area < other.area


# Problem D
# Inheritance

class House:
    def __init__(self, beds, baths, haunted):
        self.beds = beds
        self.baths = baths
        self.haunted = haunted
    def remove_ghosts(self):
        self.haunted = False
    def estimate_price(self):
        value = self.beds*3000+self.baths*2000
        if self.haunted:
            return value//2
        else:
            return value

class Mansion(House):
    def __init__(self, beds, baths):
        House.__init__(self, beds, baths, True)
    def remove_ghosts(self):
        print("Too spooky, call an expert")
    def estimate_price(self):
        return House.estimate_price(self) * 5


# Problem E
# Polymorphism

class Painting:
    def __init__(self, artist, area):
        self.artist = artist
        self.area = area

    def too_bulky(self):
        return self.area > 1000

class Sculpture:
    def __init__(self, artist, weight):
        self.artist = artist
        self.weight = weight

    def too_bulky(self):
        return self.weight > 500

def display_artist(artist, art_list):
    out = []
    for piece in art_list:
        if piece.artist == artist and not piece.too_bulky():
            out += [piece]
    return out


# Problem F
# Java

def mystery(val):
    j = 5
    i = 1
    while i < val:
        i *= 10
        j -= 1
        if j < 0:
            return 0
    return j

