from itertools import combinations

def solution(numbers):
    comb_list = list(combinations(numbers, 2))
    answer = []
    for item in comb_list:
        if sum(item) not in answer:
            answer.append(sum(item))
    return sorted(answer)