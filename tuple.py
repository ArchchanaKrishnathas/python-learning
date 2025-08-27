t = (90,70,26,90,55)
print(t)
print(type (t))

print(t[2])

#t[2]= 36           # can't modify
print(t)    

#t.append(25)
print(t)    

marks= [90,85,75,42,88]
t= tuple(marks)
print(t)
print(type (t))


marks1= (70,90,30)
marks2= (28,29,46)
marks3= marks1+ marks2
print(marks3)

# Unpacking / Data Restructuring

Student= ("Seelan", 38, "22/07/1987")
fname,age,dob= Student
print(fname)
print(age)
print(dob)

'''
Student= ("Seelan", 38, "22/07/1987")
fname,age,dob,x= Student
print(fname)
print(age)
print(dob)
print(x) '''  # error - cant unpacking . not same variable count

marks= (70,90,30,86,96)
a,*b,c= marks
print(a)
print(b)               # *b  - middle all
print(c)

marks= (70,90,30,86,96)
a,b,*c= marks
print(a)
print(b)              
print(c)



