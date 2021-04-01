from collections import deque

max = 100001
n,k = map(int, input().split())
# 간선 횟수 계산을 도와주는 리스트
array = [0] * max

# bfs를 이용
def bfs():
  q = deque([n])
  while q:
    current_pos = q.popleft()
    if current_pos == k:
      return array[current_pos]
    # 가능한 이동 경로
    for next_pos in (current_pos +1, current_pos -1, current_pos * 2):
      # 가능범위에 있고 노드에 방문하지 않았을경우
      if 0<= next_pos < max and not array[next_pos]:
        # 이전 경로 간선에 일을 더해준다
        array[next_pos] = array[current_pos] + 1
        q.append(next_pos)

print(bfs())
