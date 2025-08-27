S={"Maths","Tamil","English","Maths","Tamil"}
print(S)
print(type (S))


S.add("IT")
print(S)

'''
S.update("History")
print(S)
'''

S.update(["History","Tamil","Eng"])
print(S)
'''
S.add(["IT","Sc"])
print(S) '''  # error - cant add multiple values 

S.remove("Maths")
print(S)
'''
S.remove("Maths") # cant delete maths. it is not in set
print(S)
'''
S.discard("Tamil") # if set has , it will delete
print(S)

S.pop()   # this delete one by one at last
print(S)

S.clear()  # delete all
print(S)



# To remove duplicate values
num1=[70,80,90,80,90,55,68,75,58]
num2=set(num1)
print(num2)

# | - Union: remove duplicate, give specific values
a={1,2,3,4,5}
b={3,5,6,7,8,9}
#c=a|b              
c= a.union(b)
print(c)

#d= a&b        
d= a.intersection(b)
print(d)

e= a-b      # difference
print(e)

e= b-a
print(e)

#symmetric_difference
#f=a^b
f= a.symmetric_difference(b)
print(f)


#----------------------------------
a={1,2,3}
b={1,2,3,4,5}
c={4,5,6}

d= a|b|c
f= a&b&c

print(d)
print(f)

print(a>=b)
print(a.issubset(b))
print(b.issuperset(a))
print(b>=a)