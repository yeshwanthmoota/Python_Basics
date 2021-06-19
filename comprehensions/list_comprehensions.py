# list comprehensions.

nums=[1,2,3,4,5,6,7,8,9]

new_list=[]
for num in nums:
    new_list.append(num)
print(new_list)

# This code can be replaced by list comprehension very easily

new_list1=[num for num in nums]
print(new_list1)

# Note: If the given function is lambda-map-filter methods we should always 
# to replace them by list comprehensions which in 99% cases is possible.

# another example.

new_list=[]
for n in nums:
    new_list.append(n*n)
print(new_list)

new_list1=[n*n for n in nums]
print(new_list1)

# What if conditions are present? what to do? Let's see:

new_list=[]
for n in nums:
    if(n%2==0):
        new_list.append(n*n)
print(new_list)

new_list1=[n*n for n in nums if n%2==0]
print(new_list1)
new_list1=[n**n for n in nums]
print(new_list1)

# A more difficult example

# Let's say we want each combination from a letter from 'abcd' & a number from '012345'

my_list1=[]
for letter in 'abcd':
    for number in range(6): # that includes 0,1,2,3,4,5
        my_list1.append((letter,number)) # Here we are inserting a- 
        # -tuple (letter,number) into a list. multiple tuples into a list
print(my_list1)

# Let's do this using a list comprehension
my_list=[(letter,number) for letter in 'abcd' for number in range(6)]
print(my_list)

print(my_list==my_list1)