'''Data types are actually classes and variables are instances of those classes.In python we have the datatypes:
1.Numeric-int,float,complex
2.String-str
3.Sequence-list,tuple,range
4.Mapping-dict
5.Boolean-bool
6.Set-set,frozeenset
N.B: Use type() to see which class a variable belongs to e.g type(num1).
    Use dtype variable name and index to access value e.g languages[0] etc
'''


#NUMERIC
num_1=20          #int
num_2=34.78         #float  
num_3=1+2j          #complex
print((type(num_1),type(num_2)),type(num_3))       


#STRING-uses '' or ""
fname="Tracey"
lname='Nduta'               
print(type(fname),type(lname))

#LIST-uses [] separated by comma
languages=['Swift','Java','Python']
#Accessing values-use index
print(languages[1])     #Java

#TUPLE-uses () and  separated by comma
products=('ps5','xbox','gaming pc')
#Accessing values-use index
print(products[0])      #ps5

#SET-unordered collection of unique items. Uses {} separated by comma.Index has no meaning.
student_id={112,111,110,118,114}

#DICT-It is ordered.Uses {},separated by comma.Stores items in key/value pairs
capital_cities={'Kenya':'Nairobi','Uganda':'Kampala','Nigeria':'Abuja','Tanzania':'Dodoma'}
#Accessing values-use key eg in Kenya:Nairobi,Kenya is the key,Nairobi is the value
print(capital_cities['Kenya'])