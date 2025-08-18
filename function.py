'''
def PrintMyName():
    print("My name is Archchana")
   
PrintMyName()
'''
'''
def PrintMyName(name):
    print(f"My name is {name}")
   
PrintMyName("Archchana")
PrintMyName("Jana")
PrintMyName("Krish")
'''

'''
def PrintFullName(fname,lname):
    print(f"Your Full name is: {fname} {lname}")
  
PrintFullName("Archchana","Krish")
'''

'''
def PrintFullName(fname="Jana",lname="Jeni"):
    print(f"Your Full name is: {fname} {lname}")
  
PrintFullName()
PrintFullName("Archchana")
'''

'''
def getFullName(fname,lname):
    print(f"Your Full name is: {fname} {lname}")
    return fname+ lname
  
fullname= getFullName("Archchana","Krish")
print(fullname)
'''

def calcInterest (amount,period):
    if period == 0.25:   
        interest = amount * 12/100
    elif period == 0.5:
        interest = amount * 12.5/100
    elif period == 1:
        interest = amount * 13/100
    elif period == 3:
        interest = amount * 14/100
    elif period == 5:
        interest = amount * 15/100
    elif period >= 5:
        interest = amount * 15.5/100
    else:
        print("Invalid period")
   
    total= amount + interest    
    print(f"Interest: {interest}  Total Amount: {total}")
    #return interest,total
    
calcInterest(10000,0.25)    # 3months
calcInterest(10000,0.5)     # 6months
calcInterest(10000,1)       # 1 year
calcInterest(10000,3)       # 3 years
calcInterest(10000,5)       # 5 years 
calcInterest(10000,6)       # above 5 years
07