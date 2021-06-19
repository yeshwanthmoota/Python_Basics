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
    HELLO=0

print(__name__)
if __name__ == "__main__":
    print("OMG!!!")