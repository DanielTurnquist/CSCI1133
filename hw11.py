#Problem A.
class Complex:
    # ==========================================
    # Purpose: Each object of this class represents a complex number.
    # Instance variables: real - represents the real component of the number (float)
    # imag - represents the imaginary component of the number (float)
    # Methods: __init__(self, real, imag) - initializes an imaginary number
    # get_real(self) - returns the real component of the number
    # get_imag(self) - returns the imaginary component of the number
    # set_real(self, new_real) - changes the old real component to a new one
    # set_imag(self, new_imag) - changes the old imaginary component to a new one
    # __str__(self) - returns a formatted string representing the imaginary number
    # __add__(self, other) - adds an imaginary number to another
    # __mul__(self other) - multiplies an imaginary number to another
    # __eq__(self, other) - checks whether an imaginary number is equal to another
    # ==========================================
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def get_real(self):
        return self.real
    def get_imag(self):
        return self.imag
    def set_real(self, new_real):
        self.real = new_real
    def set_imag(self, new_imag):
        self.imag = new_imag
    def __str__(self):
        return f'{self.real} + {self.imag}i'
    def __add__(self, other):
        return Complex(self.get_real() + other.get_real(), self.get_imag() + other.get_imag())
    def __mul__(self, other):
        a = self.get_real()
        b = self.get_imag()
        c = other.get_real()
        d = other.get_imag()
        return Complex(a * c - b * d, a * d + b * c)
    def __eq__(self, other):
        return float(self.get_real()) == float(other.get_real()) and float(self.get_imag()) == float(other.get_imag())

#Problem B.
class Item:
    # ==========================================
    # Purpose: Each object in this class represents an article of clothing
    # Instance variables: name - the name of the item (string)
    # price - the price of the item (float)
    # category - the body part covered by the item (string)
    # store - the store from which the item comes (string)
    # Methods: __str__(self) - returns a formatted string representing the items characteristics
    # __lt__(self, other) - checks whether an items price is less than another's
    # ==========================================
    def __init__(self, name, price, category, store):
        self.name = name
        self.price = price
        self.category = category
        self.store = store
    def __str__(self):
        return f'{self.name}, {self.category}, {self.store}: ${self.price}'
    def __lt__(self, other):
        return self.price < other.price

class Store:
    # ==========================================
    # Purpose: each object of this class represents a clothing store
    # Instance variables: name - the name of the store (string)
    # items - the items in the store (list)
    # Methods: __init__(self, name, filename) - initializes a store object
    # __str__(self) - returns a formatted string of the store names and its items on new lines
    # ==========================================
    def __init__(self, name, filename):
        self.name = name
        self.items = []
        with open(filename, 'r') as file:
            file.readline()
            for line in file:
                line_list = line.strip().split(',')
                self.items += [Item(line_list[0], float(line_list[1]), line_list[2], self.name)]
    def __str__(self):
        output = f'{self.name}\n'
        for item in self.items:
            output += f'{str(item)}\n'
        return output

def cheap_outfit(store_list):
    output = {'Head': 0, 'Torso': 0, 'Legs': 0, 'Feet': 0}
    all_items = []
    heads = []
    torsos = []
    legss = []
    feets = []
    for store in store_list:
        all_items += store.items
    for item in all_items:
        if item.category == 'Head':
            heads += [item]
        if item.category == 'Torso':
            torsos += [item]
        if item.category == 'Legs':
            legss += [item]
        if item.category == 'Feet':
            feets += [item]
    output['Head'] = min(heads)
    output['Torso'] = min(torsos)
    output['Legs'] = min(legss)
    output['Feet'] = min(feets)
    return output