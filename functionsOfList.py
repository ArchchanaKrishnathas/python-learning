Subject= ["Maths","Tamil","English"]
#Subject[3]="IT"   cant add another into list using this way

Subject.append("IT")
print(Subject)

Subject.insert(2,"Science")
print(Subject)

Subject.extend(["Cheminstry","Physics"])
print(Subject)

Subject.pop(2)
print(Subject)

Subject.pop()
print(Subject)

Subject.remove("Tamil")
print(Subject)

if "Tamil" in Subject:
    Subject.remove("Tamil")
print(Subject)

#Subject.clear()
#print(Subject)

print(Subject.index("IT"))
#print(Subject.index("Science"))

#print(Subject.find("IT"))

Subject.sort()
print(Subject)

Subject.reverse()
print(Subject)
    
Subject.sort(reverse=True)
print(Subject)


marks= [70,20,40,95,30]
print(max(marks))
print(min(marks))
print(sum(marks))

marksD= marks.copy()
print(marksD)

marksD[2]= 45
print(marksD)
print(marks)


