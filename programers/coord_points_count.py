import math

def solution(k, d):
    i = 0
    j = 0
    count = 0

    while (i * k) ** 2 <= d ** 2:
        j = (int(math.sqrt(d ** 2 - (i * k) ** 2)) + k) // k
        print("i = {0}, j = {1}".format(i, j))
        i += 1
        count += j
    return(count)

print(solution(2, 4))
print(solution(1, 5))