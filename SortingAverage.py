stu_count = int(input("Enter number of students: "))
students = []
sub_count = int(input("\nEnter number of subjects: "))
subjects = []
student_data = []
avg_list = []

for i in range(sub_count):
    subject_name = input(f"Enter name of subject {i+1}: ")
    subjects.append(subject_name)
for i in range(stu_count):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = []
    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks.append(mark)
    total = sum(marks)
    avg = total / len(marks)
    avg_list.append(avg)
    
    if avg >= 75:
        grade = "A"
    elif avg >= 65:
        grade = "B"
    elif avg >= 55:
        grade = "C"
    elif avg >= 40:
        grade = "S"
    else:
        grade = "F"
    student_data.append([name] + marks + [total, avg, grade])
sorted_avgs = sorted(avg_list, reverse=True)
print(student_data)
print(sorted_avgs)
head = f"{'Name':<10}"
for subject in subjects:
    head += f"{subject:>8}"
head += f"{'Total':>8}{'Avg':>8}{'Grade':>8}"
print("\n" + head)
printed_avgs = []
for avg in sorted_avgs:
    for student in student_data:
        if student[-2] == avg:
            data = f"{student[0]:<10}"
            for mark in student[1:1+sub_count]:
                data += f"{mark:>8}"
            data += f"{student[-3]:>8}{student[-2]:>8.2f}{student[-1]:>8}"
            print(data)