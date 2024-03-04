'''  Submit a github repo link for the assignment below




Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.'''
# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
my_list.extend([10, 20, 30, 40])
print("Original list:", my_list)

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print("Inserted 15:", my_list)

# Extend my_list with another list: [50, 60, 70].
another_list = [50, 60, 70]
my_list.extend(another_list)
print("Appended list:", my_list)

# Remove the last element from my_list.
my_list.pop()
print("Removed last element:", my_list)

# Sort my_list in ascending order.
my_list.sort()
print("Sorted list in ascending order:", my_list)

# Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)
