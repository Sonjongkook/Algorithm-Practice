def solution(answers):
    answer = []
    scores = {1:0, 2:0, 3:0}
    
    print(answers)
    
    student1 = [1,2,3,4,5] * 2000
    student2 = [2,1,2,3,2,4,2,5] * 1250
    student3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    for i in range(len(answers)):
        if answers[i] == student1[i]:
            scores[1] += 1
        if answers[i] == student2[i]:
            scores[2] += 1
        if answers[i] == student3[i]:
            scores[3] += 1
            
    
    scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))


    # print(scores)
    max_score = 0
    for key in scores:
        print(scores[key])
        max_score = max(max_score, scores[key])
        if scores[key] == max_score:
            answer.append(key)
            
    return answer
