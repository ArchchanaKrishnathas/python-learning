s= "Welcome To Python"
print(s)
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.swapcase())
print('isAlpha ',s.isalpha())   # because,it contains space
print('isdigit ',s.isdigit())
print('islower ',s.islower())
print('isupper ',s.isupper())
print('isspace ',s.isspace())
print('startswith ',s.startswith('Welcome'))
print('endswith ',s.endswith('n'))

print(s.find('To'))    #  -1 
print(s.find('Java'))

#print(s.index('To'))
#print(s.index('Java'))
print(s.count('t'))  
print(s.replace("Python","Java"))
print(s.strip())  # cut start & end space
print(s.lstrip())  # cut start space
print(s.rstrip())   # cut last space
print(s.split())     # break as list

s= "WelcometoPython"
print('isAlpha ',s.isalpha())