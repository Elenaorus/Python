number=int(input('Введите цифру, обозначающую день недели '))
if number==7 or number==6:
  print(f"{number}-> да")
elif number>7:
  print(f'{number} не является цифрой, обозначающая день недели')
else:
  print(f'{number}-> нет')
