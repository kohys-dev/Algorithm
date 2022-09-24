def solution(price, money, count):
    answer = 0
    for c in range(1, count+1):
        answer += c * price
    
    if money < answer:
        return answer - money
    else:
        return 0

