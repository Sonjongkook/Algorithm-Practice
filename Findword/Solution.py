words = input()
search = input()


length = len(search)
idx = 0
count = 0
while idx <= len(words)-length:
  if words[idx:idx+length] == search:
    count += 1
    idx += len(search)
  else:
    idx +=1
print(count)
