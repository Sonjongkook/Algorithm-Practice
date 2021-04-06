import sys
sys.setrecursionlimit(10000)



def dfs(x, y):
  visited[x][y] = True
  # 지렁이가 갈수 있는 방향. 상하좌우
  directions = [(-1,0), (1,0), (0,1), (0,-1)]

  for j, k in directions:
    dx, dy = x + j, y + k
    if dx <0 or dx >= m or dy <0 or dy >= n:
      continue
    if land[dx][dy] and not visited[dx][dy]:
      #재귀적으로 dfs 구
      dfs(dx, dy)


t = int(input())

for _ in range(t):
  m, n, k = map(int, input().split())

  #지렁이 유무를 나타내는 이중리스트 
  land = [[0] * n for _ in range(m)]
  #방문여부를 알려주는 이중리스트 
  visited = [[False] * n for _ in range(m)]

  for _ in range(k):
    x, y = map(int, input().split())
    land[x][y] =1


  bug = 0
  # 이중리스트 순회
  for i in range(m):
    for j in range(n):
      # 땅에 지렁이가 있고 방문하지 않았을겨우 dfs 시작
      if land[i][j] and not visited[i][j]:
        dfs(i,j)
        bug += 1
  
  print(bug)
