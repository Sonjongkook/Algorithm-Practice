from collections import deque

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]


for _ in range(m):
  x,y = map(int,input().split())
  adj[x].append(y)
  adj[y].append(x)

def bfs(v):
  q = deque([v])

  while q:
    v = q.popleft()
    if not(visited[v]):
      visited[v] = True
      for e in adj[v]:
        if not visited[e]:
          q.append(e)

visited = [False] * (n+1)
bfs(1)

    

count = 0
for i in range(2,len(visited)):
  if visited[i] == True:
    count+=1 

print(count)
