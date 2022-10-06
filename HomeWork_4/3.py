from random import randint


def list_num(count):
    list_nums=[]
    if count < 0:
        print( "Negative value of the number of numbers!")
        return []
    else:
      for i in range(count):
        list_nums.append(randint(0,10))
    return list_nums
def selec(ls):
  if len(ls)>0:
      ls_sel=[]
      for i in ls:
        k=0
        for j in ls:
          if i==j:
            k+=1
        if k==1:
          ls_sel.append(i)
      return ls_sel

ls=list_num(int(input("Number of numbers: ")))
print(ls)
print(selec(ls))
      
