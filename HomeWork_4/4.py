from random import randint

def polynomial(num):
  poly=''
  
  for i in range(num,-1,-1):
      k=randint(0,10)
      if i%2==0 and i>0 and k!=0:
        poly+=str(k)+'*x^'+str(i)+'-'
      elif i%2!=0 and k!=0:
        poly+=str(k)+'*x^'+str(i)+'+'
      elif i==0 and k!=0:
        poly+=str(k)+'=0'
      elif i==0 and k==0:
        poly=poly[:-1]+'=0'
  return poly
  
  
f=open('polynom.txt','a')
for i in range(3):
  num=int(input('Enter the degree: '))
  if num>0:
    f.write(polynomial(num)+'\n')
f.close()
  
