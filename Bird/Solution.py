n = int(input())
second = 0
number =1

while True:
  if n < number:
    number = 1
  else:
    n -= number
    second += 1
    if n == 0:
      break
    number += 1

print(second)
