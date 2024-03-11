#for loop
names=['Tracey','Nduta','Chama']
for name in names:
    print(name)

numbers=[1,2,3,4,5,6,7,8,9,10]
for number in numbers:
 print(number)


 message="welcome"
 for i in range(5):
    print(message)

#break statement
colors=["White","Red","Yellow","Blue"]
colorWanted="Yellow"
for color in colors:
    if color == colorWanted:
        print("They have",color)
        break
    print(color)
   

#continue statement
   
colors=["White","Red","Yellow","Blue"]
colorWanted="Yellow"
for color in colors:
    if color == colorWanted:
        print("They have",color)
        continue
    print(color)