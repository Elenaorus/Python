x=int(input("Введите координату X: "))
y=int(input("Введите координату Y: "))
if x>0 and y>0:
  print(f"точка ({x},{y}) находится в 1 четверти")
elif x<0 and y>0:
  print(f"точка ({x},{y}) находится в 2 четверти")
elif x<0 and y<0:
  print(f"точка ({x},{y}) находится в 3 четверти")
elif x>0 and y<0:
  print(f"точка ({x},{y}) находится в 4 четверти")
elif x==0 and y!=0:
  print(f"точка ({x},{y}) находится на оси ординат")
elif y==0 and x!=0:
  print(f"точка ({x},{y}) находится на оси абсцисс")
else:
  print("точка находится в начале координат")
