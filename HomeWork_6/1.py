from random import sample


def list_num(count):
    if count < 0:
        return "Negative value of the number of numbers!"

    list_nums = sample(range(1, count*2), count)
    return list_nums


ls=list_num(int(input("Number of numbers: ")))
print(ls)

new_ls=[ls[n+1] for n in range(len(ls)-1) if ls[n]<ls[n+1]]
print(new_ls)