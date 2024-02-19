'''Python has the following operators:
1.Arithmetic
2.Assignment
3.Comparison
4.Logical
5.Bitwise
6.Special
'''
#BITWISE OPERATORS-AND(&),OR(|),NOT(~),XOR(^),>>(RIGHT SHIFT),<<(LEFT SHIFT)
'''
Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
For example, 2 is 10 in binary and 7 is 111.
In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
'''
x=10
y=4
x_left=x<<2
y_left=y<<2
x_right=x>>2
y_right=y>>2
print(x_left)       #2