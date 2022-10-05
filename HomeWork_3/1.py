from random import sample


def list_num(count):
    if count < 0:
        return "Negative value of the number of numbers!"

    list_nums = sample(range(1, count * 2), count)
    return list_nums


ls=list_num(int(input("Number of numbers: ")))


def sum_ls(ls):
  sum_num=0
  for i in range(len(ls)):
    if (i+1)%2!=0:
      sum_num+=ls[i]
  return sum_num

print(ls)
print(sum_ls(ls))
