from random import randint
n=int(input())
ls=[i for i in range(n)]
print(ls)
b=n-1
for i in range(n):
  
  s=randint(0,100)
  while s>=n:
    s=randint(0,100)
  
  f=ls[i]
  ls[i]=ls[s]
  ls[s]=f
print(ls)
