n = int(input())

for i in range(n):
    num,order = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    
    
    
    count = 0 
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count+=1
            if queue[0][1] ==order:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
