'''
y = [10,20,30,40,50]
print(y)

x= [
    [10,20,30],
    [70,90,25],
    [40,98,26]
]

print(x)
print(x[0][0])
print(x[2][2])
print(x[1][2])

i=0
while i<3:
    j=0
    while j<3:
        print(x[i][j])
        j+=1
    i+=1
'''

students=["Archana","Jana","Jeni","Jeno","Anu"]
subjects=["Maths","Physics","Chemistry"]
marks= [
    [98,56,78],
    [45,75,68],
    [95,75,85],
    [55,35,75],
    [57,68,85]
]

row= "+-----------------+-----------+-----------+-----------+------------+------------+------------+"

print(row)
print(f"| {'Student Name':<16}| {subjects[0]:<10}| {subjects[1]:<10}| {subjects[2]:<10}| {'Total':<10} | {'Average':<10} | {'Result':<10} |")
print(row)

i=0
while i< len(students):
    print(f"| {students[i]:<16}", end="")

    total=0
    j=0
    while j<len(subjects):
        print(f"| {marks[i][j]:<10}", end="")
        total+= marks[i][j]
        j+=1

    avg= total / len(subjects)

    if avg>= 75:
        result= 'A'
    elif avg>= 65:
        result= 'B'
    elif avg>= 50:
        result= 'C'
    elif avg>= 35:
        result= 'S'
    else:
        result= 'F'      

    print(f"| {total:<10} | {avg:<10.2f} | {result:<10} | ")   
    print(row)
    i+=1


