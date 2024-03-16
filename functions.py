#function to add two numbers
def sum(a,b):
    c=a+b
 
    
    #calling a function
sum()


"""#with parameters
def add_num(a,b):
    answer=a+b
    return answer
total=add_num(2,2)
print(total)


#if number of arguments is unknown
def nums(*nums):
    total_sum = 0
    count = 0
    length = len(nums)

    while count < length:
        total_sum += nums[count]
        count += 1

    return total_sum

print("Total is:", nums(1, 2, 3, 4, 5))


#if kwargs is unknown
def add_ages(**ages):
    sum=0
    for k,v in ages.items():
        sum+=v
    return sum
print("sum is:",add_ages(tracey=10,chama=21))



"""