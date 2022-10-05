def fib_list(count):
    list_nums=[]
    if count <= 0:
        print( "Negative value of the number of numbers!")
    fib=[0,1]
    for i in range(2,num+1):
          fib.append(fib[i-1]+fib[i-2])
    return fib
        

def neg_list(fib):
  neg_fib=[]
  for i in range(num+1):
    if fib[i]!=0:
      neg_fib.append(((-1)**(i+1))*fib[i])
  neg_fib.reverse()
  return neg_fib
  
num=int(input())


print(neg_list(fib_list(num))+fib_list(num))
