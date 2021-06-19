# You don't need to understand the code to understand the result. 
# focus on the result for the purpose, See which is better generators or lists.
import memory_profiler as mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# print('Memory (Before): {}Mb '.format(mem_profile.memory_usage_psutil()))
print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person


t1 = time.clock()
people = people_list(1000000) # Running the function 1 million times.(Huge input)
t2 = time.clock()
# Uncomment the above 3 lines of code and comment the below 4 to see the list's result 

# Uncomment the below 3 lines of code and comment the above 3 to see the generator's result 
# t1 = time.clock()
# people = people_generator(1000000) # Running the function 1 million times.(Huge input)
# t2 = time.clock()

# print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())
print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')

# print 'Took {} Seconds'.format(t2-t1)
print ('Took ' + str(t2-t1) + ' Seconds')