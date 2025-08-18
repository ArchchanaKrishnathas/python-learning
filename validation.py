'''
num= input("Please Enter Number: ")

while not num.isdigit():
    print("Please Re-Enter number correctly!")
    num= input("Please Enter Number: ")
print('Your number is: ', num)
'''
# first name, last name, Age, nic,    gender
import datetime

fname= input("Please Enter Your First Name: ").strip()
lname= input("Please Enter Your Last Name: ").strip()

while not (fname.isalpha() and lname.isalpha()):
    print("Invalid name! Only letters are allowed.")
    fname= input("Please Enter Your First Name: ").strip()
    lname= input("Please Enter Your Last Name: ").strip()
print("Your Fullname is: " + fname+" "+lname)

age = input("Please Enter Your Age: ").strip()

while not (age.isdigit() and 1 <= int(age) <= 100):
    print("Please re-enter age correctly!")
    age = input("Please Enter Your Age: ").strip()

print("Your age is:", age)

nic = input("Enter NIC: ").strip()
if len(nic) == 10 or len(nic) == 12:  
    if len(nic) == 12:
        boy = int(nic[:4])
        days = int(nic[4:7])             
    else:  
        boy = int("19" + nic[:2])
        days = int(nic[2:5])

    gender = "Male"
    if days > 500:
        gender = "Female"
        days -= 500
        
    print("Gender:", gender)
    
    today = datetime.date.today()
    cal_age = today.year - boy 
    
    if int(age) != cal_age:
        print("Wrong NIC! Entered age does not match NIC.")
      
   

    m_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    m= ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    
    month = ""
    date = 0
    for i in range(12):
        if days > m_days[i]:
            days -= m_days[i]
        else:
            month = m[i]
            date = days
            break

    dob = f"{boy}/{month}/{date}"
    
    print("Date of Birth:", dob)

    


    # # Convert days to month/day
    # birth_date = datetime.date(boy, 1, 1) + datetime.timedelta(days=days - 1)

    # today = datetime.date.today()
    # cal_age = today.year - boy - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    

   # print("Date of Birth:", birth_date.strftime("%Y-%m-%d"))
    
       

else:
    print("Invalid NIC. Please Try Again!")






    #     import datetime

    # def calculate_age(born):
    #     today = datetime.date.today()
    #     age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    #     return age

    # dob_string = "15/08/1990"
    # date_format = "%d/%m/%Y"
    # dob_datetime = datetime.datetime.strptime(dob_string, date_format).date() # Get only the date part
    # age = calculate_age(dob_datetime)
    # print(f"Age: {age}")