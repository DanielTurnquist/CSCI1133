## Daniel Turnquist
## turnq070

import math
# A. rotate_model
# ==========================================
# Purpose:
#   Rotates a 3d model by 90 degrees
# Input Parameter(s):
#   f_name_in is a string representing the name of a file with a non-rotated 3d model
#   fname_out is a string representing the name of the file with the rotated object
# Return Value:
#   Returns 0 if everything goes smoothly and a new file is created with the rotated model
#   OR returns -1 if the file does not exist
# ==========================================
def rotate_model(fname_in, fname_out):
    try:
        with open(fname_in, 'r') as initial_file:
            file_string = initial_file.read()
            vertex_list = file_string.strip().split('\n')
            for i, vertex in enumerate(vertex_list):
                vertex_list[i] = vertex.split()
            vertex_count = 0
            for i in range(len(vertex_list)):
                try:
                    if vertex_list[i][0] == 'v':
                        vertex_count += 1
                except IndexError:
                    ignore = 'I dont want anything to be acted on past here anyway, assuming the obj file is formatted correctly'
            for i in range(vertex_count):
                vertex_list[i][1], vertex_list[i][2] = round(float(vertex_list[i][1]) * math.cos(math.pi/2) + float(vertex_list[i][2]) * math.sin(math.pi/2), 1), round(float(vertex_list[i][2]) * math.cos(math.pi/2) + float(vertex_list[i][1]) * math.sin(math.pi/2), 1)
            for i, vertex in enumerate(vertex_list):
                for j, ele in enumerate(vertex):
                    vertex[j] = str(ele)
                vertex_list[i] = ' '.join(vertex)
            out_string = '\n'.join(vertex_list)
        with open(fname_out, 'w') as output_file:
            output_file.write(out_string)
        return 0
    except FileNotFoundError:
        return -1


# B. Part 1: get_data_list
# ==========================================
# Purpose:
#   Extract the data from a CSV file as a list of rows
# Input Parameter(s):
#   fname is a string representing the name of a file
# Return Value:
#   Returns a list of every line in that file (a list of strings)
#   OR returns -1 if the file does not exist
# ==========================================
def get_data_list(fname):
    # You MUST use a try-except block to prevent an error
    # if the file doesn’t exist
    try:
        with open(fname, 'r') as fn:
            flist = []
            for line in fn:
                flist += [line]
            return flist
    except FileNotFoundError:
        return -1

# B. Part 2: get_col_index
# ==========================================
# Purpose:
#   Determine which column stores a specific value
# Input Parameter(s):
#   row1_str is a string containing the first row of data
#   (the column titles) in the CSV file
#	col_title is a string containing the column title
# Return Value:
#   Returns the index of the column specified by col_title
#   OR returns -1 if there is no column found
# ==========================================
def get_col_index(row1_str, col_title):
    # Hint: You may use list.index(), but must
    # prevent an error if the column is not present
    try:
        row_list = row1_str.split(',')
        return row_list.index(col_title)
    except ValueError:
        return -1


# B. Part 3: convert_dkp
# ==========================================
# Purpose:
#   Covert the DKP in your row string to the new system
# Input Parameter(s):
#   row_str is a string containing any row of data from the CSV file
#   idx is an index for the column you want to alter
# Return Value:
#   Returns a string identical to row_str, except with the column
#   at the given index changed to the new DKP (as a string)
# ==========================================
def convert_dkp(row_str, idx):
    # Hint: Use .split and .join
    row_list = row_str.split(',')
    row_list[idx] = str(float(row_list[idx]) * 13.7)
    return ','.join(row_list)

# B. Part 4: merge_guild
# ==========================================
# Purpose:
#   Alters a DKP CSV file to convert DKP after a guild merger
# Input Parameter(s):
#   fname is the file name of the DKP file
# Return Value:
#   Returns False if the file isn't open
#   Returns False if the file doesn't contain 'DKP' and 'Original Guild' columns
#   Otherwise, returns True
# ==========================================
def merge_guild(fname):
    # Hints:
    #   Use get_data_list to read in the rows from the file
    #   Use get_col_index to determine which column you need to change
    #   Use get_col_index to determine which column contains the guild name
    #   Write back each row unchanged if it does not belong
    #   to a former member of the Lions of Casterly Rock
    #   If it does belong to a Lion, use convert_dkp to create an
    #   altered row string to write to the file instead
    #   Be sure to close the file
    try:
        with open(fname, 'r') as initial_csv:
            data_list = get_data_list(fname)
            guild_col = get_col_index(data_list[0], 'Original Guild')
            dkp_col = get_col_index(data_list[0], 'DKP')
            if guild_col == -1 or dkp_col == -1:
                return False
            for i in range(len(data_list)):
                data_list[i] = data_list[i].split(',')
            for data in data_list:
                if data[guild_col] == 'Lions of Casterly Rock':
                    data[dkp_col] = str(float(data[dkp_col]) * 13.7)
            for i in range(len(data_list)):
                data_list[i] = ','.join(data_list[i])
            out_string = ''.join(data_list)
        with open(fname, 'w') as file_update:
            effect = file_update.write(out_string)
            return True

    except FileNotFoundError:
        return False
