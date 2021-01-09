def solution(array, commands):
    answer = []
    for i in commands:
        temp=array[i[0]-1:i[1]] #2차원을 이렇게 표현할수가 있구나;;;; 
        temp.sort()
        answer.append(temp[i[2]-1])
    return answer
