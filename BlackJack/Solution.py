n, m = list(map(int, input().split(' ')))
card = list(map(int, input().split(' ')))

result = 0
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
             sum = card[i] +card[j] + card[k]
             if sum <= m:
                result = max(sum, result)
                
print(result)
                
