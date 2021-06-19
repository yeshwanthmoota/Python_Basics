names=["Bruce","Clark","Peter","Logan","Wade"]
heroes=["Batman","Superman","Spiderman","Wolverine","Deadpool"]
# Now to use the zip function
Identity_list=list(zip(names,heroes))
print(Identity_list)

Identity_tuple=tuple(zip(names,heroes))
print(Identity_tuple)

Identity_dict=dict(zip(names,heroes)) # This is important names goes into key and
# Heroes goes into value of each key-value pair in the dictionary.
print(Identity_dict)