def bin_num(num):
  if num < 0:
        return "Negative value!"
  ls=[]
  while num>0:
    ls.append(num%2)
    num//=2
  ls.reverse()
  for i in range(len(ls)):
    print(ls[i], end='')


bin_num(int(input('Number: ')))
#print(ls_bin_revers)

    
