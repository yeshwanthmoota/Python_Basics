#Classes and Objects

# When we create a method inside a class then the method takes in the 
# object as the first argument automatically
class Phone_store:
    
    no_of_models=0
    discount=0.20 #This is a class variable.    

    def __init__(self,company,model,price):
        self.company_name=company
        self.model_no=model
        self.price=price

        Phone_store.no_of_models+=1

    def fullname(self):
        return "{} {}".format(self.company_name,self.model_no)

print("no_of_models: ",Phone_store.no_of_models)

ph1=Phone_store("Samsung","M30",17000)
ph2=Phone_store("Apple","XR",33000)

ph1.discount=0.30

print("discount: ",Phone_store.discount)
print("discount: ",ph1.discount)
print("discount: ",ph2.discount)
print("\n")

ph1.discount=0.20 #setting back to the original value

print("discount: ",Phone_store.discount)
print("discount: ",ph1.discount)
print("discount: ",ph2.discount)
print("\n")

Phone_store.discount=0.30

print("discount: ",Phone_store.discount)
print("discount: ",ph1.discount)
print("discount: ",ph2.discount)
print("\n")


print("no_of_models: ",Phone_store.no_of_models)