s = 'Welcome to Python'
print(s)
print(len(s))
print(s[0])
print(s[-17])

i=0
while i< len(s):
    print(s[i])
    i+=1
    
i= len(s)-1
while i>= 0:
    print(s[i])
    i=i-1
    
i= -1
while i<= -len(s):
    print(s [i])
    i=i-1
   
i= - len(s)
while i<= -1:
    print(s[i])
    i+=1
    
i= -abs(len(s))
while i<= -1:
    print(s[i])
    i+=1
    
for i in s:
    print(i)
    
for i in range(len(s)-1,0,-1):
    print(i)

for i in reversed(s):
    print(i)
   
    print(reversed(s))
''' 
s[0]= 'w'
print(s)  '''

a= s[0:5]
print(a)

a= s[0:7]
print(a)

a= s[8:10]
print(a)

a= s[-17:-10]
print(a)

# please enter your DOB - find number, kooden-   error

dob= input("Please Enter your date of birth (dd/mm/yyyy): ")
#print(dob)

if len(dob)!= 10 or dob[2] != '/' or dob[5] != '/':
    print("Error: Incorrect format! Please enter as dd/mm/yyyy")
else:
    dob_nums= dob[0:2] + dob[3:5]+ dob[6:10] 
    #print(dob_nums)

    birthNum=0
    for i in range(0,2):
        birthNum= birthNum+int(dob[i])
        i+=1
    print("Birth Number:" ,birthNum)

    totNum=0
    for x in range(len(dob_nums)):
        totNum= totNum + int(dob_nums[x])
        x+=1
    if totNum % 9==0:
        print("Total Num: 9")
    else:
        print("Total Num:", totNum % 9)
        
    
      