#simple statement
snack=lambda:print("njugu")
snack()


#lambda with functions
numSquare=lambda num:num**2
print(numSquare(2))

#if string is palindrome e.g omo,madam etc
isPalindrome=lambda string : "Palindrome" if string==string[::-1] else "not palindrome"
string=input("Enter string:")
print(isPalindrome(string))