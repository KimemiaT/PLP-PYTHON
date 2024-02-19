#print statement
fname='Tracey'
lname='Nduta'
#print('Hello',fname,sep=' ',end='!\n')  #sep puts space,end moves content to the next line

#user input
userIn=int(input('Enter your USERID:')) #prompt user to enter USERID
users={111:'Joy',222:'Jim',333:'Annie'}  #dict to save userid:name as key:value pair
print('Hello',users[userIn],'.','Welcome',sep=' ',end='!\n')
