from decimal import Decimal
num=input('Enter a real number: ')
toh=input('Enter the required accuracy 0.0001: ')
n=Decimal(num)
print(n.quantize(Decimal(toh)))
