'''
CONVERSION-There are two types of conversion:
1.Implicit-auto-conversion.
2.Explicit-manual conversion.(Type-casting)
'''
#IMPLICIT-(auto-conversion)
a=1.34
b=3
c=a+b
print(type(c)) #will be auto-converted to type float to accomodate the dps and to avoid data loss

#EXPLICIT-also known as typecasting(done manually)
x=8
y='12'
y=int(y)        #changes y from str to int
z=x+y
print(z)

'''COMMENTS-There are two types of comments:
1.Single-line i.e #
2.Multi-line i.e either using triple single quotes or using triple double quotes as in this comment!.
Pros:
1.Makes code easier to understand
2.Used for debugging
'''
#Single line comment
'''Multiple line comment'''
