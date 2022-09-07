def isbalanced(p):
    cnt = 0
    for item in p:
        if item == '(':
            cnt += 1
        else:
            cnt -= 1
    if cnt == 0: 
        return True
    else: 
        return False


def iscorrect(p):
    test_list = []
    for item in p:
        if not test_list:
            test_list.append(item)
        else:
            if test_list[-1] + item == '()':
                test_list.pop()
            else:
                test_list.append(item)
    if not test_list: 
        return True
    else: 
        return False


def solution(p):
    answer, u, v = '', '', ''
    
    # 빈 문자열이거나 올바른 괄호 문자열일 경우 문자열 반환 
    if len(p) == 0 or iscorrect(p):
        return p
    
    for i in range(2, len(p)+1, 2):
        is_u = p[:i]
        if isbalanced(is_u):
            u = is_u
            v = p[i:]
            break
    
    if iscorrect(u):
        answer += u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for item in u[1:-1]:
            print(item)
            if item == '(': answer += ')'
            else: answer += '(' 
        
    return answer
        
    