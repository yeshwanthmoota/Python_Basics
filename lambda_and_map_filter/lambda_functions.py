# We write lambda functions when we don't want to officially define a function 
# Using def we can even define lambda inside another function and work with it
# It's scope is only limited to the function in which it is defined in that case.
# We use lambda incase we don't want to reuse the function in anyway or we need the function 
# just for a single purpose or something.

def func(n):
    return n*n
print(func(2))

func= lambda n: n*n # Here we are naming the anonymous function with the name func.
print(func(2))

def func1(x,y=7):
    return x*y

print(func1(4,7))
print(func1(5))

func1 = lambda x,y=7:x*y

print(func1(4,7))
print(func1(5))

# see more applications of lambda functions in map_filter.py
