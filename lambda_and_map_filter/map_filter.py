nums=[1,2,3,4,5,6,7,8,9]
def double(n):
    return n*2

my_list=map(double,nums)
print(my_list)

def even1(n):
    return n%2==0
def even2(n):
    if(n%2==0):
        return n
my_list=map(even2,nums) #This doesn't return a list it returns- 
#-address of the genrators of the operation performed.
print(my_list)

my_list=list(map(even2,nums))
print(my_list)

# If we don't want to actually define a function just for 
# single purpose we can use lamda functions.
my_list=list(map(lambda n: n*n,nums))
print(my_list)
# with map we cannot decide which to choose i mean see below

my_list=list(map(lambda n: n%2==0,nums))
print(my_list)
# The Output is "[False, True, False, True, False, True, False, True, False]"
# But that is not we wanted we wanted to print "[2, 4, 6, 8]"
# For this we have to select the elements for which n%2==0 is true for that purpose
# We have filter function it appends the element to the list if the 
# condition in the function section comes out to be true.

my_list=list(filter(lambda n: n%2==0,nums))
print(my_list)
# Now the Output is "[2, 4, 6, 8]" as we expected.

my_list=list(map(lambda n: n*n,nums))
print(my_list)