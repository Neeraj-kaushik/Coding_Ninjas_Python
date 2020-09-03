num=int(input())
digit=num
sumofeven=0
sumofodd=0
while digit!=0:
    x=digit%10
    if x%2==0:
        sumofeven+=x
    else:
        sumofodd+=x
    digit=digit//10
print(sumofeven," ",sumofodd)