import time


list = []
incrementL = []

num = 1
increment = 1

for i in range(0, int(input("")) + 1):
  list.append(num)
  num *= 2

list.sort(reverse=True)

print(list)