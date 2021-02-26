n = int(input())

num_list = []

for i in range(n):
  num = int(input())
  num_list.append(num)

def findCount(array):  
  tallest = array[0]
  count = 1 
  for n in range(1, len(array)):
    if tallest < array[n]:
      tallest = array[n]
      count += 1
  return count

print(findCount(num_list))
num_list.reverse()
print(findCount(num_list))
