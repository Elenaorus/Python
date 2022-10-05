from random import sample


def list_num(count):
    if count < 0:
        return "Negative value of the number of numbers!"

    list_nums = sample(range(1, count * 2), count)
    return list_nums
def mult_num(ls):
  if len(ls)%2==0:
    count=len(ls)//2
  else:
    count=len(ls)//2+1
  ls_mult=[]
  for i in range(count):
    
    if i<(len(ls)//2):
      ls_mult.append( ls[i]*ls[len(ls)-1-i])
    else:
      ls_mult.append( ls[i])
  return ls_mult
ls=list_num(int(input('Number of numbers: ')))
print(ls)
print(mult_num(ls))
    

