number=int(input("Введите номер черверти"))
if number==1:
  print("х пренадлежит (0;1000000000) и y пренадлежит (0;100000000)")
elif number==2:
  print("х пренадлежит (-1000000000;0) и y пренадлежит (0;100000000)")
elif number==3:
  print("х пренадлежит (-1000000000;0) и y пренадлежит (-1000000000;0)")
elif number==4:
  print("х пренадлежит (0;1000000000) и y пренадлежит(-1000000000;0) ")
else:
  print("Введен не верный номер четверти")
  
