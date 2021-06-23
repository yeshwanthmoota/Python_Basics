#Classes and Objects

# When we create a method inside a class then the method takes in the 
# object as the first argument automatically
#--------------------------------------------------------------------
class Phone_store:
    
    no_of_models=0 #This is a class variable.
    discount=0.20 #This is a class variable.    

    def __init__(self,company,model,price):
        self.company_name=company
        self.model_no=model
        self.price=int(price)

        Phone_store.no_of_models+=1

    def details(self):
        print("{}---{}\nprice: {}\ndiscount: {}%".format(self.company_name,self.model_no,self.price,(self.discount)*100))
        print("-------------------------")
    
    @classmethod
    def discount_alter(cls,amt):
        cls.discount=(amt if (amt<1) else amt/100)
#--------------------------------------------------------------------
ph1=Phone_store("Samsung","M30",17999)
ph2=Phone_store("Apple","XR",33999)
ph3=Phone_store("Samsung","M20",12999)
ph4=Phone_store("Xiaomi","Redmi K20 Pro",23499)
ph5=Phone_store("Realme","C20",6799)
ph6=Phone_store("POCO","M3","10999")

print(ph6.details())
print(Phone_store.details(ph6))
print(ph4.details())
Phone_store.discount_alter(30) #30%
print(ph6.details())
print(ph4.details())
Phone_store.discount_alter(0.25) #25%
print(Phone_store.details(ph6))
print(Phone_store.details(ph4))
#--------------------------------------------------------------------