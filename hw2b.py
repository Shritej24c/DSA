# BT3051 Assignment 2b
# Roll number: BE14B004
# Collaborators: None
# Time: 1:00


def binary_to_decimal():
    f = open("hw2b_input.csv", 'r')
    final_list = []
    l = []
    p = []
    numb = 0
    for line in f.readlines():
        numbers = line.strip('\n').split(",")
        l.append(len(numbers))
        for num in numbers:
            dec = 0
            if len(num) >= 4:
                for i in range(4):
                    if num[3 - i] == "1":
                        dec += 2**i
                    else:
                        pass
                final_list.append(dec)
            else:
                pass
    f.close()
    final_list.sort()
    for j in range(len(l)):
        numb += l[j]
        p.append(numb)
    for i in p:
        final_list[i - 1] = str(final_list[i - 1]) + "\n"
    output = ', '.join(str(x) for x in final_list)
    lines = output.split("\n")
    final_lines = [lines[0]]
    for j in range(1, len(lines)):
        test = lines[j]
        final_line = test[2:]
        final_lines.append(final_line)
    final_output = '\n'.join(final_lines)
    f_output = open('hw2b_output.csv', 'w')
    f_output.write(final_output)
    f.close()


binary_to_decimal()


