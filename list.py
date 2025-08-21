'''Subject = ["Maths","Tamil","English","Science","IT"]
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

i=0
while i< len(Subject):   
    Subject[i]= input(f"Which Subject want to change for {Subject[i]}: ")
    i+=1
print (Subject)
print(Subject[1:3])
print(Subject[3:5]) 
print(Subject[:3])
print(Subject[2:])
print(Subject[::2])
print(Subject[::3])'''



'''
Salary= [45500,50000,100000,200000,225000,250000,275000,300000,325000,60000,400000,500000]
months= ["January","February","March","April","May","June","July","August","September","October","Novermebr","December"]

tax=0
netSalary=0
totalSalary=0
totalTax=0
totalNetSalary=0
i=0
while i< len(Salary):
    if Salary[i] < 50000:
        tax= Salary[i] * 3/100
    elif 50000 <= Salary[i] < 100000:
        tax= Salary[i] * 5/100
    elif 100000 <= Salary[i] < 300000:
        tax= Salary[i] * 8/100
    elif 300000 <= Salary[i]:
        tax= Salary[i] * 10/100
        
    netSalary = Salary[i]- tax
    print("Months Salary  Tax        Net Salary")
    print(f"{months[i]}   {Salary[i]} {tax}  {netSalary}")
    
    totalSalary += Salary[i]
    totalTax += tax
    totalNetSalary += netSalary
    i+=1
print("-------------------------------------------------------------------")
print(f"Total Salary: {totalSalary} Total Tax: {totalTax} Total Net Salary: {totalNetSalary}")

'''

'''
# using \t
Salary= [45500,50000,100000,200000,225000,250000,275000,300000,325000,60000,400000,500000]
months= ["January","Febru","March","April","May","June","July","August","Septemb","October","Novemb","Decem"]
tax=[0,0,0,0,0,0,0,0,0,0,0,0]

netSalary=0
totalSalary=0
totalTax=0
totalNetSalary=0

print("Months\t\tBasic Salary\tTax\t\tNet Salary")
print("---------------------------------------------------------------")

i=0
while i< len(Salary):
    if Salary[i] < 50000:
        tax[i]= Salary[i] * 3/100
    elif 50000 <= Salary[i] < 100000:
        tax[i]= Salary[i] * 5/100
    elif 100000 <= Salary[i] < 300000:
        tax[i]= Salary[i] * 8/100
    elif 300000 <= Salary[i]:
        tax[i]= Salary[i] * 10/100
        
    netSalary = Salary[i]- tax[i]
    
    print(f"{months[i]}\t\t{Salary[i]}\t\t{tax[i]}\t\t{netSalary}")
    
    totalSalary += Salary[i]
    totalTax += tax[i]
    totalNetSalary += netSalary
    i+=1
print("---------------------------------------------------------------")
print(f"Total\t\t{totalSalary}\t\t{totalTax}\t{totalNetSalary}")
'''

'''
Salary= [45500,50000,100000,200000,225000,250000,275000,300000,325000,60000,400000,500000]
months= ["January","February","March","April","May","June","July","August","September","October","November","December"]
tax=[0,0,0,0,0,0,0,0,0,0,0,0]

netSalary=0
totalSalary=0
totalTax=0
totalNetSalary=0

print(f"{'Month':<10} {'Basic Salary':<14} {'Tax':<12} {'Net Salary':<14}")
print("---------------------------------------------------------------")

i=0
while i< len(Salary):
    if Salary[i] < 50000:
        tax[i]= Salary[i] * 3/100
    elif 50000 <= Salary[i] < 100000:
        tax[i]= Salary[i] * 5/100
    elif 100000 <= Salary[i] < 300000:
        tax[i]= Salary[i] * 8/100
    elif 300000 <= Salary[i]:
        tax[i]= Salary[i] * 10/100
        
    netSalary = Salary[i]- tax[i]
    
    print(f"{months[i]:<10} {Salary[i]:<14}{tax[i]:<14}{netSalary:<14}")
    
    totalSalary += Salary[i]
    totalTax += tax[i]
    totalNetSalary += netSalary
    i+=1
print("---------------------------------------------------------------")
print(f"{'Total':<10}{totalSalary:<14}{totalTax:<14}{totalNetSalary:<14}")
'''

Salary= [45500,50000,100000,200000,225000,250000,275000,300000,325000,60000,400000,500000]
months= ["January","February","March","April","May","June","July","August","September","October","November","December"]
tax=[]

netSalary=0
totalSalary=0
totalTax=0
totalNetSalary=0

print(f"{'Month':<10} {'Basic Salary':<14} {'Tax':<12} {'Net Salary':<14}")
print("---------------------------------------------------------------")

i=0
while i< len(Salary):
    if Salary[i] < 50000:
        tax[i]= Salary[i] * 3/100
    elif 50000 <= Salary[i] < 100000:
        tax[i]= Salary[i] * 5/100
    elif 100000 <= Salary[i] < 300000:
        tax[i]= Salary[i] * 8/100
    elif 300000 <= Salary[i]:
        tax[i]= Salary[i] * 10/100
        
    netSalary = Salary[i]- tax[i]
    
    print(f"{months[i]:<10} {Salary[i]:<14}{tax[i]:<14}{netSalary:<14}")
    
    totalSalary += Salary[i]
    totalTax += tax[i]
    totalNetSalary += netSalary
    i+=1
print("---------------------------------------------------------------")
print(f"{'Total':<10}{totalSalary:<14}{totalTax:<14}{totalNetSalary:<14}")