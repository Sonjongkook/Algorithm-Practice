n = int(input())
book_dic = {}

for _ in range(n):
  book = input()
  try:
     book_dic[book] += 1
  except KeyError:
      book_dic[book] =1

# 리스트 컴프레션을 이용해 가장 최대값을 가진 키를 
max_list = [k for k,v in book_dic.items() if max(book_dic.values()) == v]
max_list.sort()
print(max_list[0])
