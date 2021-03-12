import heapq

n = int(input())
heap = []

for _ in range(n):
  heapq.heappush(heap, int(input()))

result = 0

while len(heap) != 1:
  #Pick out by 2 
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)

  sum_value = one + two
  result += sum_value
  #append it to the heap
  heapq.heappush(heap, sum_value)

print(result)
