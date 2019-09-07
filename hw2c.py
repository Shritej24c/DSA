# BT3051 Assignment 2c
# Roll number: BE14B004
# Collaborators: None
# Time: 1:15

import string


def password_check():
    f = open("hw2c_input.csv", 'r')
    final_list = []
    upper = list(string.ascii_uppercase)
    n_upper = 0
    lower = list(string.ascii_lowercase)
    n_lower = 0
    special = ['$', '!', '@']
    n_special = 0
    n_int = 0
    n_space = 0
    for line in f.readlines():
        passwords = line.split(",")
        for password in passwords:
            if 4 <= len(password) <= 8:
                for i in range(len(password)):
                    if password[i] in [str(x) for x in range(10)]:
                        n_int += 1
                    elif password[i] in upper:
                        n_upper += 1
                    elif password[i] in lower:
                        n_lower += 1
                    elif password[i] in special:
                        n_special += 1
                    elif password[i] == " ":
                        n_space += 1
                    else:
                        pass
                if n_int > 0 and n_upper > 0 and n_lower > 0 and n_special > 0 and n_space == 0:
                    final_list.append(password)
                else:
                    pass
            else:
                pass
    f.close()
    output = ', '.join(final_list)
    lines = output.split("\n")
    final_lines = [lines[0]]
    for j in range(1, len(lines)):
        test = lines[j]
        final_line = test[2:]                   # indexing of the lines from second element to get rid of the ", " appearing at the start of every line except for the first line
        final_lines.append(final_line)
    final_output = '\n'.join(final_lines)
    f_output = open('hw2c_output.csv', 'w')
    f_output.write(final_output)
    f.close()


password_check()
