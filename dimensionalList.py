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

print(f"'Student Name':<14,{subjects}")