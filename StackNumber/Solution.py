num_list=[*open(0)]
n=int(num_list[0])
num_list=[*map(int,num_list[1:])]

stack = [0]
i = 1
list_record = 0 
answer = []
avail = True

while stack and list_record< len(num_list):
  if stack[-1] == num_list[list_record]:
    stack.pop()
    answer.append("-")
    list_record+=1
  else:
    stack.append(i)
    i+=1
    answer.append("+")
  if(i>n+1):
    avail = False
    print("NO")
    break

if(avail):
  for word in answer:
    print(word)
