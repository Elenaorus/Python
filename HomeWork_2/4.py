a=int(input('Position one '))
b=int(input('Position two '))
n=int(input('Number of elements: '))

k=[]
for i in range(n+1):
  k.append(i)
  if i>0:
    
    k.append(i*(-1))
k=sorted(k)
print(k)
if a<=(n*2) and b<=(n*2):
  print(k[a-1]*k[b-1])
else:
  print('Error')

