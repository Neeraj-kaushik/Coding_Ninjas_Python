"""here th epattern is 
   1
   11
   121
   1221"""
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if j==1 or j==i:
            print('1',end='')
        else:
            print('2',end='')
        j=j+1
    print()
    i=i+1