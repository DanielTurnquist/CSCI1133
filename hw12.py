#Problem A.

class Adventurer:
    # ==========================================
    # Purpose: each object of this class represents a character in a turn-based RPG

    # Instance variables: name - the name of the character (string)
    # level - the character's level value (integer)
    # strength - how strong the character is (integer)
    # speed - how fast the character is (integer)
    # power - how powerful the character is (integer)
    # HP - how many hitpoints the character has (integer)
    # hidden - whether the character is hidden (Boolean)

    # Methods: __repr__(self) - returns a formatted string with the character's name and HP level
    # attack(self, other) - reduces another characters HP by some value
    # __lt__(self, other) - determines whether a characters HP is less than another character's HP, returns Boolean
    # ==========================================
    def __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = self.level * 6
        self.hidden = False
    def __repr__(self):
        return f'{self.name} - HP: {self.HP}'
    def attack(self, other):
        if other.hidden:
            print(f'{self.name} can\'t see {other.name}')
        else:
            other.HP -= self.strength + 4
            print(f'{self.name} attacks {other.name} for {self.strength + 4} damage')
    def __lt__(self, other):
        return self.HP < other.HP

class Thief(Adventurer):
    # ==========================================
    # Purpose: an object in this class represents a type of adventurer, namely a thief
    # Instance variables: HP - number of hitpoints the thief has (integer)
    # hidden - whether the thief is hidden (Boolean)
    # Methods: attack(self, other) - reduces another adventurers HP by some value
    # ==========================================
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level * 8
        self.hidden = True
    def attack(self, other):
        if not self.hidden:
            Adventurer.attack(self, other)
        else:
            other.HP -= (self.speed + self.level) * 5
            self.hidden = False
            other.hidden = False
            print(f'{self.name} sneak attacks {other.name} for {(self.speed + self.level) * 5} damage')

class Ninja(Thief):
    # ==========================================
    # Purpose: each Ninja object is a specialized Thief object
    # Instance variables: HP - number of hitpoints the ninja has (integer)
    # hidden - whether the ninja is hidden (Boolean)
    # Methods: attack(self, other) - reduces another adventurers HP by some value
    # ==========================================
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level * 8
        self.hidden = True
    def attack(self, other):
        Thief.attack(self, other)
        self.hidden = True
        self.HP += self.level

class Mage(Adventurer):
    # ==========================================
    # Purpose: a Mage is a specialized type of adventurer
    # Instance variables: fireballs_left - the number of fire balls the mage still has (integer)
    # Methods: attack(self, other) - reduces another adventurers HP by some value
    # ==========================================
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.fireballs_left = self.power
    def attack(self, other):
        if self.fireballs_left == 0:
            Adventurer.attack(self, other)
        else:
            other.HP -= self.level * 3
            other.hidden = False
            self.fireballs_left -= 1
            print(f'{self.name} casts a fireball on {other.name} for {self.level * 3} damage')

class Wizard(Mage):
    # ==========================================
    # Purpose: A wizard is a specialized type of mage
    # Instance variables: HP - how many hitpoints the wizard has (integer)
    # fireballs_left - the number of fire balls the wizard still has (integer)
    # Methods: attack(self, other) - reduces another adventurers HP by some value
    # ==========================================
    def __init__(self, name, level, strength, speed, power):
        Mage.__init__(self, name, level, strength, speed, power)
        self.HP = self.level * 4
        self.fireballs_left = self.power * 2
    def attack(self, other):
        Mage.attack(self, other)

#Problem B.

def battle(player_list, enemy_list):
    while len(player_list) > 0 and len(enemy_list) > 0:
        print('\n----------Player Turn----------\nYour team:')
        for adventurer in player_list:
            print(adventurer)
        print('')
        i = 1
        for enemy in enemy_list:
            print(f'Enemy  {i} : {enemy}')
            i += 1
        for adventurer in player_list:
            if len(enemy_list) != 0:
                target = input(f'choose a target for {adventurer.name}:')
                adventurer.attack(enemy_list[int(target) - 1])
                if enemy_list[int(target) - 1].HP <= 0:
                    print(f'{enemy_list[int(target) - 1].name} was defeated!')
                    del enemy_list[int(target) - 1]
            if len(player_list) != 0 and len(enemy_list) != 0:
                print('')
            j = 1
            if adventurer != player_list[-1]:
                for enemy in enemy_list:
                    print(f'Enemy  {j} : {enemy}')
                    j += 1
        if len(enemy_list) > 0:
            print('----------Enemy Turn----------')
        if len(player_list) != 0:
            for enemy in enemy_list:
                enemy.attack(min(player_list))
                if min(player_list).HP <= 0:
                    print(f'{min(player_list).name} was defeated!')
                    player_list.remove(min(player_list))
        if len(player_list) == 0:
            print('You lose!')
        elif len(enemy_list) == 0:
            print('You win!')


