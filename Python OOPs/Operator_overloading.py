import math
#-------------------------------------------------------------
class Complex:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b

        
    def __add__(self,other):
        return Complex(self.a + other.a, self.b + other.b)


    def __sub__(self,other):
        return Complex(self.a - other.a, self.b - other.b) 


    def __mul__(self,other):
        return Complex(((self.a*other.a)-(self.b*other.b)),((self.a*other.b)+(self.b*other.a))) 


    def __truediv__(self,other):
        u=self.a
        v=self.b
        x=other.a
        y=other.b
        temp=((self)*(Complex(x,-y)))
        temp.a=temp.a/((x**2)+(y**2))
        temp.b=temp.b/((x**2)+(y**2))

        return temp

    def __eq__(self,other):
        if(self.a==other.a) and (self.b==other.b):
            return True
        else:
            return False


    def __lt__(self,other):
        u=self.a **2
        v=self.b **2
        x=other.a **2
        y=other.b **2
        if((u+v)<(x+y)):
            return True    
        else:
            return False

    def __gt__(self,other):
        u=self.a **2
        v=self.b **2
        x=other.a **2
        y=other.b **2
        if((u+v)>(x+y)):
            return True    
        else:
            return False


    def __le__(self,other):
        u=self.a **2
        v=self.b **2
        x=other.a **2
        y=other.b **2
        if((u+v)<=(x+y)):
            return True    
        else:
            return False
    

    def __ge__(self,other):
        u=self.a **2
        v=self.b **2
        x=other.a **2
        y=other.b **2
        if((u+v)>=(x+y)):
            return True    
        else:
            return False

    def val_eq(self,other):
        u=self.a**2
        v=self.b**2
        x=other.a**2
        y=other.b**2
        if((u+v)==(x+y)):
            return True    
        else:
            return False
    def __str__(self):       # Important method.  # Overloading the print method.
        return "{}+({})i".format(self.a,self.b)
    def __len__(self):
       # This function return type needs to be an int
        return int(math.sqrt(self.a**2 + self.b**2))
#-------------------------------------------------------------
c1=Complex(1,-3)
c2=Complex(1,2)
c3=Complex(4,1)

print(c1)
print(c2)

print(c1 + c2)
# OR
c4=c1+c2

# OR
print(c4)

print(c1*c2)

print(c1/c2)

print(c1==c3)
print(c1==c2)
print(c1<=c3)
print(c1<c2)
print(c3>=c3)
print(c2>c3)
print()
print(Complex.val_eq(c1,c3))
print(len(c3))