import queue

def solution (X, Y):
    q = queue.PriorityQueue()
    num1 = {0 : 0,
           1 : 0,
           2 : 0,
           3 : 0,
           4 : 0,
           5 : 0,
           6 : 0,
           7 : 0,
           8 : 0,
           9 : 0}
    num2 = {0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
            6 : 0,
            7 : 0,
            8 : 0,
            9 : 0}
    ans = ""
    
    
    for i in range(len(X)) :
        num1[int(X[i])] += 1
    for i in range(len(Y)) :
        if num1[int(Y[i])] > 0 :
            num1[int(Y[i])] -= 1
            num2[int(Y[i])] += 1
    for i in range(9, 0, -1) :
        while num2[i] > 0 :
            ans += str(i)
            num2[i] -= 1
    return (str(ans))

print(solution("1234", "321"))