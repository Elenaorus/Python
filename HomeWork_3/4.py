from random import uniform


def list_num(count):
    list_nums=[]
    if count <= 0:
        print( "Negative value of the number of numbers!")
        return [0.0]
    for i in range(count):

      list_nums.append( round(uniform(1, 10),2))
    return list_nums



def min_num(ls):
  mi_ls=ls[0]
  for i in range(1,len(ls)):
    if ls[i]<mi_ls:
      mi_ls=ls[i]
  return mi_ls

def max_num(ls):
  ma_ls=ls[0]
  for i in range(1,len(ls)):
    if ls[i]>ma_ls:
      ma_ls=ls[i]
  return ma_ls

ls=list_num(int(input()))
print(ls)
print(f"Min: {min_num(ls)}, Max: {max_num(ls)}, Difference: {round(max_num(ls)-min_num(ls),2)}")

