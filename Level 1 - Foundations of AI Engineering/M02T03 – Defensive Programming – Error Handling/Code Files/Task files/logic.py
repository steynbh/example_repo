# create an arrow pattern using asterisks with a for loop that points to the right
for i in range(1, 6):
    # print asterisks in a way that forms an arrow shape
    print(' ' * (5 - i) + '*' * (2 * i - 1))
    