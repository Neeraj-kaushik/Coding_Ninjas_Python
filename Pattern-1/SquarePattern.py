##pattern is if value is 4 then pattern is 
"""4444
   4444
   4444
   4444"""

n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print(n,end='')
        j=j+1
    print()
    i=i+1