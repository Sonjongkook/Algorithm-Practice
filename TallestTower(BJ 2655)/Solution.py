n = int(input())

# 벽돌 리스트
array = []

# 다이내믹 프로그래밍 진행을 위한 열 추가
array.append((0,0,0,0))


for i in range(1, n+1):
  width, height, weight = map(int, input().split())
  array.append((i, width, height, weight))

# 무게를 바탕으로 정렬
array.sort(key=lambda x : x[3])

# dp 계산을 위한 리스트 
dp = [0] * (n+1)

# 각각의 벽돌이 제일 밑에 있을때의 최대높이를 구하는 과정
for i in range(1,n+1):
  for j in range(i):
    if array[j][1] < array[i][1]:
      dp[i] = max(dp[i], dp[j] + array[i][2])

# 역추적 방식으로 벽돌 정보 
max_value = max(dp)
index = n
result = []

while index != 0:
  if max_value == dp[index]:
    result.append(array[index][0])
    max_value -= array[index][2]
  index -= 1

result.reverse()

print(len(result))
[print(i) for i in result] 
