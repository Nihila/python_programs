n=int(input("enter value :"))
temp=n
rev=0
while(n>0):
    r=n%10
    rev=(rev*10)+r
    n=n//10
print (rev)
if(temp == rev):
    print("the number is palindrome :")
else:
    print("not a palindrome :")
    
            
