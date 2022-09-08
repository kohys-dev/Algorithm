from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        course_menu = []
        for order in orders:
            course = combinations(sorted(order), c)
            course_menu += course
        cnt = Counter(course_menu)
        if len(cnt) != 0 and max(cnt.values()) != 1:
            answer += [''.join(f) for f in cnt if cnt[f] == max(cnt.values())]
            
    return sorted(answer)