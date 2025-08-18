'''
for x in range (10):
    if x % 2== 1:
        print(x, end=' ')
    
for x in range(1, 11):
    if x % 2 == 0:
        print(x, end=' ')

for x in range(1, 6):
    print( x * (x+1) // 2 , end=" ")

for x in range (1, 6):
    print(x*x, end=' ')

for x in range(1, 6):
    if x % 2 == 1:
        print(x, end=' ')
    else:
        if x % 2 == 1:
           print('*', end=' ')

for x in range (1,6):
    if x % 2== 1:
        print(x, '*')
    else: 
        print(x,'**')

for x in range(5):
    for y in range(1, 6):
        print(y,end=' ')
    print()

for x in range(5):
    for y in range(5,0,-1):
        print(y,end=' ')
    print()

for x in range(5,0,-1):
    for y in range(5):
        print(x,end=' ')
    print()

for x in range(1,6):
    for y in range(5):
        print(x,end=' ')
    print() 

for x in range(5):
    for y in range(5):
        print('*',end=' ')
        if x==y:
            break           
    print()

for x in range(1,6):
    for y in range(1,6):
        print(y,end=' ')
        if x==y:
            break
    print()             '''

for x in range(1,6):
    for y in range(1, x+1):
        print(y,end=' ')
    print()