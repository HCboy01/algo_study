def solution(s):
    ls = list(s.split(' '))
    sum = 0
    for i in range(len(ls)):
        if ls[i] == 'Z' :
            sum -= int(ls[i - 1])
        else :
            sum += int(ls[i])
    return (sum)

print(solution("1 2 Z 3"))