# BT3051 Assignment 2d
# Roll number: BE14B004
# Collaborators: None
# Time: 0:15


def armstrong():
    numbers = []
    for i in range(1, 1000):
        string = str(i)
        cube = 0
        for j in range(len(string)):
            cube += int(string[j])**3
        if i == cube:
            numbers.append(i)
    armstrong_numbers = ','.join(str(x) for x in numbers)            # converted into comma separated string
    print(armstrong_numbers)


armstrong()
