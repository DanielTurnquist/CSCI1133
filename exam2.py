## Daniel Turnquist
## turnq070

#Problem A
def findq(str_list):
    q_count = 0
    for string in str_list:
        if 'q' in string or 'Q' in string:
            q_count += 1
    return q_count

#Problem B
def long_lists(nested_list):
    out = []
    for list in nested_list:
        if len(list) >= 3:
            out += [list]
    return out

#Problem C
def parens_split(phrase):
    out = []
    in_parens = False
    string = ''
    for ch in phrase:
        if ch == ')':
            in_parens = False
            out += [string]
            string = ''
        if in_parens:
            string += ch
        if ch == '(':
            in_parens = True
    return out


#Problem D
def get1_3(filename):
    try:
        with open(filename, 'r') as fn:
            rows = []
            for line in fn:
                rows += [line]
            for i, row in enumerate(rows):
                rows[i] = row.split(',')
            return int(rows[0][2])
    except FileNotFoundError:
        return 0

#Problem E
def remove_t(fname):
    with open(fname, 'r') as fn:
        contents = fn.read()
        output_string = ''
        for ch in contents:
            if ch != 't':
                output_string += ch
    with open('no_t_' + fname, 'w') as nt:
        nt.write(output_string)