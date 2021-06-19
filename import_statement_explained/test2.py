# import test1
# ph1=test1.Phone("Samsung","M30",17000)
# ph2=test1.Phone("Apple","XR",33000)

# print(ph1.fullname())
# print(ph2.fullname())


# from test1 import * 
# OR 
from test1 import Phone as ph 
ph1=ph("Samsung","M30",17000)
ph2=ph("Apple","XR",33000)

print(ph1.fullname())
print(ph2.fullname())