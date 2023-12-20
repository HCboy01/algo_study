import math

def solution(left, right):
    sum = 0
    for i in range(left, right + 1) :
        if int(math.sqrt(i)) ** 2 == i:
            sum -= i
        else :
            sum += i
    return (sum)

print(solution(13, 17))