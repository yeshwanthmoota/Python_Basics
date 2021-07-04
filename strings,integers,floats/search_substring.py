# program to find a sub-string within a string.
def search_substring(string,substring):
    count=0
    for i in range(len(string)):
        count=0
        if(string[i]==substring[0]):
            count=1
            for j in range(len(substring)):
                if((i+j)==len(string)): # crossed the limits of string=>not present in the string. 
                    count+=1
                    break
                if(string[i+j]!=substring[j]):
                    count+=1
                    break
            if(count==1):  # This is only true case all the remaining are false.
                return i # it is present at the i'th position in the list.
    return -1 # else all false cases return -1 .
            


def check(x):
    if x==-1:
        print("The substring is not present in the main string.")
    else:
        print("The substring {} is found at {} position in the string {}.".format(substring,x,string))


print("Enter a string: ")
string=input()
print("Enter a substring u want to search: ")
substring=input()
x=search_substring(string=string,substring=substring)
check(x)

