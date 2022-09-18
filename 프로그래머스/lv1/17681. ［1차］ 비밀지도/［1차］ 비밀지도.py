from queue import deque

def get_binary(num, lists):
    a, b = divmod(num, 2)
    lists.appendleft(b)
    if a == 0:
        return lists
    else:
        return get_binary(a, lists)
    

def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        x_2 = deque([], maxlen=n)
        y_2 = deque([], maxlen=n)
        x_binary = get_binary(x, x_2)
        y_binary = get_binary(y, y_2)
        while len(x_binary) < n:
            x_binary.appendleft(0)
        while len(y_binary) < n:
            y_binary.appendleft(0)
        line = []
        for i in range(len(x_binary)):
            if x_binary[i] == y_binary[i] == 0:
                line.append(' ')
            else:
                line.append('#')
        answer.append(''.join(line))
    return answer