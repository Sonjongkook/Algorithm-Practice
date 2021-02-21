
#O(Nlogn)의 시간 복잡도가 필요! quick sort는 최악의 경우 O(N^2)이므로 이 문제에는 부적절..

# Solution1(Using Merge sort)
def merge(left, right):
  merged_list = []

  left_idx = 0
  right_idx = 0
  while left_idx < len(left) and right_idx < len(right):
    if left[left_idx] <= right[right_idx]:
      merged_list.append(left[left_idx])
      left_idx += 1
    else:
      merged_list.append(right[right_idx])
      right_idx += 1

  if(left_idx == len(left)):
    merged_list += right[right_idx:]

  if(right_idx  == len(right)):
    merged_list += left[left_idx:]

  return merged_list

def merge_sort(array):
  if len(array) <= 1:
    return array
  mid = len(array)//2

  return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))

test_num = int(input())
num_list = []
for _ in range(test_num):
    num = int(input())
    num_list.append(num)

num_list = merge_sort(num_list)

for i in num_list:
    print(i)
    


#Solution2 Using Python Sort method
n = int(input())

num_list =[]
for _ in range(n):
    num = int(input())
    num_list.append(num)

num_list.sort() 

for k in num_list:
    print(k)
    
    
    
