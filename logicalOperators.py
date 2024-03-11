'''Python has the following operators:
1.Arithmetic
2.Assignment
3.Comparison
4.Logical
5.Bitwise
6.Special'''

#LOGICAL OPERATORS-AND,OR,NOT      1-ON  0-OFF
print( True and True)       #True
print(False and False)      #False
print( True and  False)     #False
print(True or False)        #True
print(not True)             #False
print(not False)            #True



age=int(input("Enter age:"))
gender=input("Enter your gender:")
gender=gender.upper().lower()
#AND-Male only  club(football club)
if(age>=18 and gender is not'Female'):
 print("Allowed to join")
else:
 print("Not allowed to join")
