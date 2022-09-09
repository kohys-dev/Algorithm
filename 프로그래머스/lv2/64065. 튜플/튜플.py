def solution(s):
    answer = []
    sub = s.replace("},", " ").replace('{', '').replace('}', '')
    t = sorted(sub.split(' '), key=len)
    for item in t:
        if ',' in item:
            k = item.split(',')
            for num in k:
                if num not in answer:
                    answer.append(num)
        else:
            answer.append(item)
    return list(map(int, answer))

