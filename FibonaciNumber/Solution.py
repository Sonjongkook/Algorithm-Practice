
//Using dynamic programming
def Fibonaci(num):
    fib_dic = {}
    fib_dic[0] = 0
    fib_dic[1] = 1
    
    for i in range(2, num+1):
        fib_dic[i] = fib_dic[i-1] + fib_dic[i-2]
        
    return fib_dic[num]

print(Fibonaci(int(input())))
