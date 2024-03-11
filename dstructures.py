list=[1,2,3,4,5]      #mutability
#number 2 is index 1
list[1]=1
#print(list)
  
"""tple=(1,2,3,4,5)    #immutable
#number 1 is index 0
tple(0)=0
print(tple)"""
languages=['python','swift','c++']
#print('first method:',languages[1])
#print('second method:',languages[-2])
letters=['c','h','a','m','a']
#print(letters)
#print(letters[:3])

#append()
numbers=[1,2,3]
letters=['c','h','a','m','a']
numbers.append(4)

#extend()
letters.extend(numbers)
#print(letters)


fName='Tee'
lName='Dboy'
print(fName+lName)

#del
del letters[1]
#remove
letters.remove("m")
#print(letters)
#reverse()
name=['Chama','Tee']

print('original list:',name)
name.reverse()
print('reversed list',name)
#iterating through list
countries=['Kenya','Zambia','Uganda','Nigeria']
'''for country in countries:
     if country is not 'Uganda':
     # print(country)'''
number=[number*number for number in range(1,5)]   
#print(number)

greetings=("Hello")
salut=("Bonjour",)
print(type(greetings))
print(type(salut))


#tuple    index(),count()

countries=('Kenya','Zambia','Kenya','Nigeria')
countryIndex=countries.index('Nigeria')
countryCount=countries.count('Kenya')
#print(countryCount)

countries={1:'Kenya',2:'Zambia',3:'Uganda',4:'Nigeria'}
#adding elements
countries[5]='Rwanda'
#removing elements
del countries[3]
#replace elements
countries[1]='Ghana'
print(countries)
