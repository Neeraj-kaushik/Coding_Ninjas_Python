"""here the pattern is 
   E
   DE
   CDE
   BCDE
   ABCDE"""

n=int(input())
i=1
p=n
while i<=n:
    j=1
    start_char=chr(ord('A')+p-1)
    while j<=i:
        charj=chr(ord(start_char)+j-1)
        print(charj,end='')
        j=j+1
    p=p-1
    print()
    i=i+1