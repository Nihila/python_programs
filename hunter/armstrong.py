r=int(input("enter the value :"))
a=r
n=0
while(r>0):
    rem=r%10
    rem=rem**3
    r=r//10
    n=rem+n
print(n)
if(n==a):
    print("armstrong")
else:
    print("not armstong")   
    
