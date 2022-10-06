def simple_divisor(n):
   i = 2
   ls = []
   while i * i <= n:
       while n % i == 0:
           ls.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       ls.append(n)
   return ls
print(simple_divisor(int(input())))
