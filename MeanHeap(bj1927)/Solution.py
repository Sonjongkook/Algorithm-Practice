
# 1. 힙을 직접 구현 

class Heap:
  def __init__(self):
    self.heap_array = list()
    self.heap_array.append(None)
    
  def move_up(self, inserted_idx):
    if inserted_idx <= 1:
      return False
    
    parent_idx = inserted_idx//2
    if self.heap_array[inserted_idx] < self.heap_array[parent_idx]:
      return True
    else:
      return False

  def insert(self,data):
    if len(self.heap_array) == 0:
      self.heap_array.append(None)
      self.heap_array.append(data)
      return True
    
    self.heap_array.append(data)

    #힙의 성질이 맞는지 검증 
    inserted_idx = len(self.heap_array) -1

    while self.move_up(inserted_idx):
      parent_idx = inserted_idx//2
      self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
      inserted_idx = parent_idx

  def move_down(self, poped_idx):
    left_child_poped_idx = poped_idx *2
    right_child_poped_idx = (poped_idx*2) +1

    #case1:왼쪽 자식 노드도 없을때
    if left_child_poped_idx >= len(self.heap_array):
      return False
    #case2:오른쪽 자식 노드만 없을때
    elif right_child_poped_idx >= len(self.heap_array):
      if self.heap_array[poped_idx] > self.heap_array[left_child_poped_idx]:
        return True
      else:
        return False
    #case3: 왼쪽 오른쪽 자식 노드 모두 있을때
    else:
      if self.heap_array[left_child_poped_idx] < self.heap_array[right_child_poped_idx]:
        if self.heap_array[poped_idx] > self.heap_array[left_child_poped_idx]:
          return True
        else:
          return False
      else:
        if self.heap_array[poped_idx] > self.heap_array[right_child_poped_idx]:
          return True
        else:
          return False

  
  def pop(self):
    if len(self.heap_array) <=1:
      print(0)
      return None

    returned_data = self.heap_array[1]
    self.heap_array[1] = self.heap_array[-1]
    del self.heap_array[-1]
    poped_idx = 1

    while self.move_down(poped_idx):
      left_child_poped_idx = poped_idx *2
      right_child_poped_idx = poped_idx *2 +1

      #case2:오른쪽 자식 노드만 없을때
      if right_child_poped_idx >= len(self.heap_array):
        if self.heap_array[poped_idx] > self.heap_array[left_child_poped_idx]:
            self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] =  self.heap_array[left_child_poped_idx], self.heap_array[poped_idx]
            poped_idx = left_child_poped_idx
      #case3: 왼쪽 오른쪽 자식 노드 모두 있을때
      else:
        if self.heap_array[left_child_poped_idx] < self.heap_array[right_child_poped_idx]:
          if self.heap_array[poped_idx] > self.heap_array[left_child_poped_idx]:
            self.heap_array[poped_idx], self.heap_array[left_child_poped_idx] =  self.heap_array[left_child_poped_idx], self.heap_array[poped_idx]
            poped_idx = left_child_poped_idx
        else:
          if self.heap_array[poped_idx] > self.heap_array[right_child_poped_idx]:
            self.heap_array[poped_idx], self.heap_array[right_child_poped_idx] =  self.heap_array[right_child_poped_idx], self.heap_array[poped_idx]
            poped_idx = right_child_poped_idx

    print(returned_data)
    return returned_data
  
test_num = int(input())

heap = Heap()

for _ in range(test_num):
  n = int(input())
  if n == 0:
    heap.pop()
  else:
    heap.insert(n)
    
    
# 2. heapq 라이브러리를 이용한 솔루션

import heapq

n = int(input())

heap = []
result = []

for _ in range(n):
  data = int(input())
  if data == 0:
    if heap:
      result.append(heapq.heappop(heap))
    else:
      result.append(0)
  else:
    heapq.heappush(heap, data)

for data in result:
  print(data)

 
    
