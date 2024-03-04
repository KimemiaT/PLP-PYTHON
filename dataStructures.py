'''Tasks:

Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.'''

#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
# Accept user input to create a list of integers
input_values = input("Enter a list of integers separated by spaces: ")

# Convert the input string to a list of integers
try:
    user_list = [int(x) for x in input_values.split()]
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
    exit()

# Compute the sum of all the integers in the list
sum_of_integers = sum(user_list)

# Display the result
print("List of integers:", user_list)
print("Sum of integers:", sum_of_integers)
#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
favBooks=("book1","book2","book3",'book4','book5')
for book in favBooks:
    print(book)
#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
myDict={}
name=input("Enter name:")
age=input("Enter your age:")
myDict[name]=age
print(myDict)
#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
setOneInput = input("Enter a set of integers separated by spaces: ")
setTwoInput = input("Enter a set of integers separated by spaces: ")
# Convert the input string to a set of integers
#set one
setOne = {int(x) for x in setOneInput.split()}
#set two
setTwo = {int(x) for x in setTwoInput.split()}
#join set one and two to print common elements
newSet=setOne.intersection(setTwo)
print(newSet)
#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.'''
wordslist = ["apple", "banana", "orange", "kiwi", "grape"]
words_len=[len(wordslist[0]),len(wordslist[1]),len(wordslist[2]),len(wordslist[3]),len(wordslist[4])]
newList=[word for word in wordslist if len(word) % 2 != 0]
print(newList)
  