#if else statement
age=int(input("Enter your age:"))
if age >=18:
    print("Access Granted")
else:
    print("Access Denied")


#NESTED IF...elif
age=int(input("Enter your age:"))
if age >35:
 print("ADULT")
elif age <=35 and age >21:
   print("YOUTH")
elif age >=21 and age <35:
   print("YOUNG ADULT")
elif age >=18:
   print("LEGAL AGE")
elif age >=13:
   print("TEENAGER")
elif age >11:
   print("PRETEEN")
elif age <=10:
   print("CHILD!")


