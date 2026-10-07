n=int(input("Enter number of n terms: "))
if n<=0:
    print("Fibonacci series upto ",n," is not defined")
else:
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
