def solution(prices):
# deque 구조를 사용할시에 효율성 테스트를 통과 못해서 인덱스를 iterate 해서 풀이
    answers =[]
    
    for i in range(len(prices)):
        second = 0
        for j in range(i+1, len(prices)):
            second += 1
            if prices[i] > prices[j]:
                answers.append(second)
                second = 0
                break
            if j == len(prices)-1:
                answers.append(second)
    
    answers.append(0)
    return answers
