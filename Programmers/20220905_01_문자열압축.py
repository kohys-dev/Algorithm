def solution(s):
    answer = len(s)
    for i in range(1, len(s)):
        cnt = 1
        prev = ''
        length = 0

        for j in range(0, len(s), i):
            temp = s[j:j + i]
            if prev == temp:
                cnt += 1
            elif prev != temp:
                length += len(temp)
                if cnt > 1:
                    length += len(str(cnt))
                cnt = 1
                prev = temp
        if cnt > 1:
            length += len(str(cnt))

        answer = min(answer, length)

    return answer