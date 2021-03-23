def solution(numbers):
    numbers.sort()
    
    num = -99999999999
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            num = numbers[i] + numbers[j] 
            if num not in answer:
                answer.append(num)
                
    answer.sort()
            
        
    return answer
