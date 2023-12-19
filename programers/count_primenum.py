import math

def solution(nums):
    size = len(nums)
    i = count = flag = 0

    while (i < size) :
        a = nums[i]
        j = i + 1
        while (j < size) :
            b = nums[j]
            k = j + 1
            while (k < size) :
                flag = 0
                c = nums[k]
                num = a + b + c
                for t in range(2, int(math.sqrt(num)) + 2) :
                    if num % t == 0:
                        flag = 1
                        break
                if flag == 0 :
                    count += 1
                k += 1
            j += 1
        i += 1
    return (count)

solution([1,2,7,6,4])