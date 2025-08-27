students=[]
subjects=[]
average=[]
st_data=[]

st_count =int(input("Enter the number of students: "))
sub_count = int(input("Enter the number of subjects: "))

for i in range(sub_count):
    sub= input(f"Enter the subject {i+1}:")
    subjects.append(sub)

for x in range(st_count):
    st_name= input(f"Enter the name of student {x+1}:")
    students.append(st_name)

    marks = []
    for subject in subjects:
        m = int(input(f"Enter the marks of {subject}:"))
        marks.append(m)
    
    total= sum(marks)
    avg= total/sub_count
    average.append(avg)

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
    
    st_data.append([st_name]+ marks + [total, avg, result])

print(st_data)
sorted_avg= sorted(average, reverse=True)
print(sorted_avg)

head=(f"{'Student name':<16}")
for sub in subjects:
    head+= (f"{sub:>10}")
head+= (f"{'Total':>10}{'Average':>10}{'Result':>10}")
print(head)

for avg in sorted_avg:
    for data in st_data:
        if data[-2]== avg:
            sorted_data= (f"{data[0]:<16}")
            for mark in data[1:1+sub_count]:
                sorted_data+= (f"{mark:>10}")
            sorted_data+= (f"{data[-3]:>10}{data[-2]:>10.2f}{data[-1]:>10}")
            print(sorted_data)



        


# x=0
# while x < n:
#     name = input(f"Enter the name of student {x+1}: ")
#     students.append(name)
    
#     n1 =int(input(f"How many subjects has {name} taken? "))
    
#     y=0
#     while y < n1:
#         sub = input(f"Enter the name of subject {y+1} for {name}: ")
#         subjects.append(sub)  
        
#         student_marks=[]
#         m = input(f"Enter the marks of {sub}: ")
#         student_marks.append(m)
#         y += 1
#         marks.append(student_marks) 
#     x += 1

# print(students)
# print(subjects)
# print(marks)


# print(row)
# #print(f"| {'Student Name':<16}| {subjects[0]:<10}| {subjects[1]:<10}| {subjects[2]:<10}| {'Total':<10} | {'Average':<10} | {'Result':<10} |")
# print(row)

# i=0
# while i< len(students):
#     print(f"| {students[i]:<16}", end="")

#     total=0
#     j=0
#     while j<len(subjects):
#         print(f"| {marks[i][j]:<10}", end="")
#         total+= marks[i][j]
#         j+=1

#     avg= total / len(subjects)

    # if avg>= 75:
    #     result= 'A'
    # elif avg>= 65:
    #     result= 'B'
    # elif avg>= 50:
    #     result= 'C'
    # elif avg>= 35:
    #     result= 'S'
    # else:
    #     result= 'F'      

#     print(f"| {total:<10} | {avg:<10.2f} | {result:<10} | ")   
#     print(row)
#     i+=1

