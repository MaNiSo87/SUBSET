x = int(input('The number of members of the collection: '))
binary = []
list = []
for _ in range(x):
    list.append(int(input()))
for _ in range(x):
    binary.append(0)
print('[]')
for _ in range(pow(2,x) - 1):
    index = x
    while True:
        index -= 1
        if binary[index] == 0:
            binary[index] = 1
            break
        else:
            binary[index] = 0 
    print('[',sep='',end='')
    b = False
    for i in range(x):
        if binary[i] == 1 and b == True:
            print(',',sep='',end='')
            print(list[i],sep=' ',end='')
        elif binary[i] == 1 and b == False:
            print(list[i],sep='',end='')
            b = True
    print(']',sep='',end='\n')

print()
ans = input('Do you want the binaries? ')
if ans == 'yes':
    for i in range(x):
        print(0,sep='',end='')
    print()
    for _ in range(pow(2,x) - 1):
        index = x
        while True:
            index -= 1
            if binary[index] == 0:
                binary[index] = 1
                break
            else:
                binary[index] = 0
        for i in binary:
            print(i,sep='',end='')
        print()
else:
    print('OK, have a good day :)')

