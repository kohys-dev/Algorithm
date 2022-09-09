from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    hit = 0
    miss = 0
    cache = deque(maxlen=cacheSize)
    
    for item in cities:
        item = item.lower()
        if item in cache:
            hit += 1
            cache.remove(item)
            cache.appendleft(item)
        else:
            miss += 1
            cache.appendleft(item)

    answer = hit * 1 + miss * 5
    return answer