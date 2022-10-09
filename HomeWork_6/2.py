count=int(input('Number of numbers: '))
if count < 20:
       print("Negative value of the number of numbers!")
else:
    ls=[i for i in range(20,count+1)]
    

    new_ls=[n for n in ls if n%20==0 or n%21==0]
    print(new_ls)