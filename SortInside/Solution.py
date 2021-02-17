num_list = input()

for i in range(9, -1, -1):
    for j in num_list:
        if(i == int(j)):
            print(i, end='')
