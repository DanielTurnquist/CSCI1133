#Problem A
def string_initialize():
    # ==========================================
    # Purpose: prints 5 lines of the string "Who needs loops?".
    # Input Parameter(s): None
    # Return Value(s): None
    # ==========================================
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")

def string_multiply():
    # ==========================================
    # Purpose: calls on string_initialize() six times.
    # Input Parameter(s): None
    # Return Value(s): None
    # ==========================================
    string_initialize()
    string_initialize()
    string_initialize()
    string_initialize()
    string_initialize()
    string_initialize()

def print_121():
    # ==========================================
    # Purpose: Prints 121 lines of the string "Who needs loops?".
    # Input Parameter(s): None
    # Return Value(s): None
    # ==========================================
    string_multiply()
    string_multiply()
    string_multiply()
    string_multiply()
    print("Who needs loops?")

#Problem B
def choice(text, optionA, optionB, optionC):
    # ==========================================
    # Purpose: Allows a user to make a choice between three options, given a prompt.
    # Input Parameters:
    #   text: This is what the user is prompted with.
    #   optionA: This is the first of three options available to the user.
    #   optionB: This is the second of three options available to the user.
    #   optionC: This is the third of three options available to the user.
    # Return Value(s): None
    # ==========================================
    print(text)
    print("")
    print("A.", optionA)
    print("B.", optionB)
    print("C.", optionC)
    user_selection = input("Choose A, B, or C: ")
    if user_selection == "A":
        return "A"
    elif user_selection == "B":
        return "B"
    elif user_selection == "C":
        return "C"
    else:
        print("Invalid option, defaulting to A")
        return "A"

#Problem C
def adventure():
    # ==========================================
    # Purpose: Allows a user to play a text adventure game.
    # Input Parameter(s): None
    # Return Values:
    # True (for a good outcome)
    # False (for a bad outcome)
    # ==========================================
    test_chamber = 1
    if test_chamber == 1:
        decision = choice("You awake in a small cell to the sound of an upbeat radio tune.\n"
                          "A female voice says something about tests and serious injuries.\n"
                          "Then, a portal opens behind you.\n"
                          "You...",
                          "Go back to bed",
                          "Place the radio in the toilet",
                          "Go through the portal")
        if decision == "A":
            test_chamber += 1
        elif decision == "B":
            print("You free your ears, but at what cost?\n"
                  "(You get electrocuted)")
            return False
        elif decision == "C":
            test_chamber += 2

    if test_chamber == 2:
        decision = choice("You fall asleep.\n"
                          "\n"
                          "(Years pass)\n"
                          "\n"
                          "You wake up in a massive complex filled with empty beds.\n"
                          "You see some signs leading in different directions...\n"
                          "You...",
                          "Go back to sleep",
                          "Follow the sign labeled \"Glad0s chamber\"",
                          "Follow the sign labeled \"Testing chamber\"")
        if decision == "A":
            print("You dream of cake for the rest of time.\n There are worse fates.")
            return True
        elif decision == "B":
            test_chamber += 2
        elif decision == "C":
            test_chamber += 1

    if test_chamber == 3:
        decision = choice("You find a gun that shoots portals. You could call it a \"portal shooter\" "
                          "You turn a corner, and another female voice says\n"
                          "\"There you are\"\n"
                          "And you hear bullets whizz by!\n"
                          "You...",
                          "Tell them you're a pacifist",
                          "Use your nifty device to destroy the turrets",
                          "Pick one of the turrets up")
        if decision == "A":
            print("They don't share your principled position on violence\n"
                  "(You confirm the efficacy of Aperture manufactured bullets)")
            return False
        elif decision == "B":
            test_chamber += 1
        elif decision == "C":
            print("You grab a turret from behind, and threaten to kill it if it doesn't shoot on your command.\n"
                  "Frightened, it agrees.\n"
                  "You go on a murderous rampage through the facility and straight up shoot Glad0s.\n"
                  "Years later you get interviewed by the NRA.")
            return True

    if test_chamber == 4:
        decision = choice("You find Glad0s, the female voice from before.\n"
                          "She starts to fill the room with a deadly neuro-toxin,\n"
                          "and you know you have mere minutes to act.\n"
                          "You...",
                          "Find a way to destroy the cores attached to her",
                          "Find a potato and transfer her into it",
                          "Try to find a way out")
        if decision == "A":
            print("You monster. Those cores were really cute.\n"
                  "You win.")
            return True
        elif decision == "B":
            print("I'm not really sure how this worked without Wheatly, but whatever.\n"
                  "You win.")
            return True
        elif decision == "C":
            print("There's no way out!\n"
                  "You die by deadly neuro-toxin.")
            return False
