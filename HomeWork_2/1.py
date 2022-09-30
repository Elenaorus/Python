number=input("Введите число")
k=len(number)-1
n=float(number)*10**k
s=0
while n>0:
  s+=n%10
  n//=10
print(s)
  
