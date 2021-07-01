# A
def convert(notes, up):
    # ==========================================
    # Purpose: Moves each note in a list of notes up or down a given number of octaves.
    # Input Parameter(s): notes - A list of musical notes.
    # up - How many octaves up or down to shift each note.
    # Return Value(s): A list of the shifted notes.
    # ==========================================
    scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    conversion_nums = []
    for note in notes:
        conversion_nums += [scale.index(note) + up]
    for ind in range(len(conversion_nums)):
        if conversion_nums[ind] < 0 or conversion_nums[ind] >= 12:
            conversion_nums[ind] = conversion_nums[ind] % 12
    conversion = []
    for num in conversion_nums:
        conversion += [scale[num]]
    return conversion


# B
def triple_sum(num_lst, target):
    # ==========================================
    # Purpose: Prints all unique combinations of three numbers in a given list,
    # and returns the total number of unique combinations.
    # which add up to a given target number.
    # Input Parameter(s): num_lst - List of numbers.
    # target - Number which is the desired sum to add the other three numbers up to.
    # Return Value(s): The total number of unique combinations.
    # ==========================================
    sums = 0
    for i in range(len(num_lst)):
        for j in range(i, len(num_lst)):
            for k in range(j, len(num_lst)):
                if num_lst[i] + num_lst[j] + num_lst[k] == target and i != j != k:
                    print(f"{num_lst[i]} + {num_lst[j]} + {num_lst[k]} = {target}")
                    sums += 1
    return sums


# C
def no_front_teeth(names_list):
    # ==========================================
    # Purpose: Arranges and returns a list of names such that every other name has an 's' or a 'z',
    # or let's the user know that this is not possible.
    # Input Parameter(s): names_list - List of names to be arranged.
    # Return Value(s): A list of names alternating between those with and without an 's' or 'z',
    # or an empty list if this is not possible.
    # ==========================================
    odd_names = []
    odd_index = 0
    even_names = []
    even_index = 0
    output = []
    out_of_evens = False
    for name in names_list:
        if 's' in name or 'z' in name or 'S' in name or 'Z' in name:
            even_names += [name]
        else:
            odd_names += [name]
    if len(odd_names) < len(even_names):
        print("Mission impossible: too many unpronounceable names")
        return []
    for i in range(len(names_list)):
        if i % 2 == 1 and even_index in range(len(even_names)):
            output += [even_names[even_index]]
            even_index += 1
        elif i % 2 == 1 and even_index not in range(len(even_names)):
            out_of_evens = True
        if i % 2 == 0 and not out_of_evens:
            output += [odd_names[odd_index]]
            odd_index += 1
        elif out_of_evens:
            output += [odd_names[odd_index]]
            odd_index += 1
    return output
