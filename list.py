Subject = ["Maths","Tamil","English","Science","IT"]
print(Subject)
print(Subject[0])
print(Subject[-5])
print(len(Subject))

i=0
while i< len(Subject):
    print (Subject[i])
    i+=1

print(type (Subject))

Subject[0]= "History"
print(Subject)
'''
i=0
while i< len(Subject):   
    Subject[i]= input(f"Which Subject want to change for {Subject[i]}: ")
    i+=1
print (Subject)
'''
print(Subject[1:3])
print(Subject[3:5]) 
print(Subject[:3])
print(Subject[2:])
print(Subject[::2])
print(Subject[::3])