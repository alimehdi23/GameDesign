
size= 8
for line in range(size):
    print()
    for number in range(line+1):
        print("*", end = '')
    for space in range(size-line-1):
        print('', end='')
    for number in range(size-line):
        print("*", end='')
    for space in range(size-line-1):
        print('', end='')
        
