from itertools import combinations

def solution(numbers):
    comb_list = list(combinations(numbers, 2))
    answer = []
    for item in comb_list:
        answer.append(sum(item))
    return sorted(set(answer))