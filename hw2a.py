# BT3051 Assignment 2a
# Roll number: BE14B004
# Collaborators: None
# Time: 1:30


def capitalise_first_letter():
    f = open("hw2a_input.csv", 'r')
    final_list = []
    l = []
    p = []
    num = 0
    for line in f.readlines():
        words = line.strip('\n').split(",")
        l.append(len(words))
        for word in words:
            a = word[0].upper()
            capital_word = a + word[1:]
            final_list.append(capital_word)
    final_list.sort()
    f.close()
    for j in range(len(l)):
        num += l[j]
        p.append(num)
    for i in p:
        final_list[i-1] += "\n"
    output = ', '.join(final_list)
    lines = output.split("\n")
    final_lines = [lines[0]]
    for j in range(1, len(lines)):
        test = lines[j]
        final_line = test[2:]
        final_lines.append(final_line)
    final_output = '\n'.join(final_lines)
    f_output = open('hw2a_output.csv', 'w')
    f_output.write(final_output)
    f.close()


capitalise_first_letter()
