"""here the pattern is 
   A
   BC
   CDE
   DEFG"""

n=int(input())
i=1
while i<=n:
    j=1
    start_char=chr(ord("A")+i-1)
    while j<=i:
        chart=chr(ord(start_char)+j-1)
        print(chart,end='')
        j=j+1
    print()
    i=i+1
    