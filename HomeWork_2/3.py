n=int(input())
k=[]
for i in range(1,n+1):
  h=round((1+1/i)**i)
  k.append(h)


print(k)
print(sum(k))
