n=int(input("enter the lower range :"))
r=int(input("enter the upper range :"))
for i in range(n,r+1):
    sum=0
    temp=i
    while temp>0:
        c=temp%10
        sum=sum+c**3
        temp=temp//10
    if i==sum:
        print(i)
