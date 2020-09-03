n=int(input())
while(True):
    if n==1:
        a=int(input())
        b=int(input())
        sum=a+b
        print(sum)
    elif n==2:
        a=int(input())
        b=int(input())
        dif=a-b
        print(dif)
    elif n==3:
        a=int(input())
        b=int(input())
        product=a*b
        print(product)
    elif n==4:
        a=int(input())
        b=int(input())
        qut=int(a/b)
        print(qut)
    elif n==5:
        a=int(input())
        b=int(input())
        rem=a%b
        print(rem)
    elif n==6:
        break
    else:
        print("Invalid Operation")
    n=int(input())