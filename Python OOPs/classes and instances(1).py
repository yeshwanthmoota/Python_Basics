#Classes and Objects

# When we create a method inside a class then the method takes in the 
# object as the first argument automatically
class Phone:
    
    def __init__(self,company,model,price):
        self.company_name=company
        self.model_no=model
        self.price=price
    def fullname(self):
        return "{} {}".format(self.company_name,self.model_no)

ph1=Phone("Samsung","M30",17000)
ph2=Phone("Apple","XR",33000)

print(ph1.fullname())
print(ph2.fullname())

