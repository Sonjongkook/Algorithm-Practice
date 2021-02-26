n,m = map(int, input().split())

castle_list = []

for i in range(n):
  castle_list.append(input())

target_row =n
for x in range(n):
  for y in range(m):
    if castle_list[x][y] == "X":
      target_row -= 1
      break


target_col = m
for y in range(m):
  for x in range(n):
    if castle_list[x][y] == "X":
      target_col -= 1
      break

print(max(target_row, target_col))
