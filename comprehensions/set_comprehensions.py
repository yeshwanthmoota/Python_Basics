nums=[1,34,2,1,54,23,34,2,2,6,13,53]
my_set=set()
for num in nums:
    my_set.add(num)
print(my_set)

# Now using set comprehension

my_set1={num for num in nums} #Just as list comp and dict comp
# we can add conditions and nested loops at the end of set comp.
print(my_set1)