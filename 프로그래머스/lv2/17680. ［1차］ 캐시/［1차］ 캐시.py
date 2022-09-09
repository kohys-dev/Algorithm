from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    hit = 0
    miss = 0
    cache = deque()
    
    for item in cities:
        item = item.lower()
        if item in cache:
            hit += 1
            cache.remove(item)
            cache.appendleft(item)
        else:
            miss += 1
            if len(cache) < cacheSize:
                cache.appendleft(item)
            else:
                cache.pop()
                cache.appendleft(item)

    answer = hit * 1 + miss * 5
    return answer