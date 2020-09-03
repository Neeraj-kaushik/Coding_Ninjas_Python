num=int(input())
rev=0
digit=num
while digit!=0:
    rev=rev*10
    rev=rev+digit%10
    digit=digit//10
if rev==num :
    print("true") 
else:
    print("false") 