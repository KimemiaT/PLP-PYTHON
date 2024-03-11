"""#while loop
score=0
while score <=5:
    print(score)
    score+=1"""


#break statement
colors=["White","Red","Yellow","Blue"]
colorWanted="Yellow"
length=len(colors)
count=0
while count < length and count <=5:

 print(colors[count])
 if colors[count] == colorWanted:
        print("They have yellow")
        break
count+=1
   

#continue statement
   
colors=["White","Red","Yellow","Blue"]
colorWanted="Yellow"
length=len(colors)
count=0
while count < length and count <=5:
    if colors[count] == colorWanted:
        print("They have yellow")
        continue
count+=1
    