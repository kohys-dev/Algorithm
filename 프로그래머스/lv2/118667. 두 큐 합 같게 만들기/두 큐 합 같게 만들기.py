def solution(queue1, queue2):
    answer = -1
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target = (sum1 + sum2)//2
    i, j, t = 0, 0, len(queue1)
    
    while i < 2*t and j < 2*t and sum1!=sum2:
        if sum1 < target:
            sum1 += queue2[j]
            sum2 -= queue2[j]
            queue1.append(queue2[j])
            j += 1
        else:
            sum1 -= queue1[i]
            sum2 += queue1[i]
            queue2.append(queue1[i])
            i += 1
    if sum1 == target:
        answer = i+j
    return answer