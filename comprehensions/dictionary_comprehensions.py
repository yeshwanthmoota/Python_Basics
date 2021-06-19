# Make sure to go through zip_function.py before reading this file.


names=["Bruce","Clark","Peter","Logan","Wade"]
heroes=["Batman","Superman","Spiderman","Wolverine","Deadpool"]

my_dict=dict(zip(names,heroes)) # This is important names goes into key and
# Heroes goes into value of each key-value pair in the dictionary.
print(my_dict,"\n")

# OR

my_dict1={}
print("list of heroes and identities: \n",list(zip(names,heroes)),"\n")
for name,hero in list(zip(names,heroes)):
    my_dict1.update({name:hero}) # we can directly assign or use update method.
print(my_dict1,"\n")
# OR 
my_list=list(zip(names,heroes))
print(my_list,"\n")
for name,hero in my_list: # for loops unpacks 2 values from my_list inside each tuple
    my_dict1[name]=hero # directly assignment of values to respective keys.
print(my_dict1,"\n")

# Now Using dictionary comprehension.
names=["Bruce","Clark","Peter","Logan","Wade"]
heroes=["Batman","Superman","Spiderman","Wolverine","Deadpool"]

my_dict2={name:hero for name,hero in list(zip(names,heroes))}
print("Using dictionary comprehension: \n",my_dict2)

# If we don't want to add Peter then

my_dict2={name:hero for name,hero in list(zip(names,heroes)) if name!="Peter"}
print("Using dictionary comprehension: \n",my_dict2)
