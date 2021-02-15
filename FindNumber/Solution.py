n = int(input())
n_list = set(map(int, input().split(' ')))

m = int(input())
m_list = list(map(int, input().split(' ')))

for num in m_list:
    if num not in n_list:
        print('0')
    else:
        print('1')
