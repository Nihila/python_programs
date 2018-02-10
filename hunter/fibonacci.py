a=int(input("enter first value :"))
b=int(input("enter second value :"))
l=int(input("enter the limit :"))
print(a,b,end=" ")
while(l-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    l=l-1
