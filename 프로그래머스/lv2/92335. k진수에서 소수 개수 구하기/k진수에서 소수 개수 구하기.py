# 1. n을 k진수로 변경
# 2. 변경한 숫자에서 0이 아닌 숫자 추출
# 3. 소수 판별

def convert_k(n, k):
    k_num_reversed = ''
    while n > 0:
        n, mod = divmod(n, k)
        k_num_reversed += str(mod)
    return k_num_reversed[::-1]


def isprime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True


def solution(n, k):
    prime_cnt = 0

    # n을 k진수로 변경
    k_num = convert_k(n, k)
    
    # 0이 아닌 숫자 추출
    is_prime_num = [item for item in k_num.split('0') if item != '']
    
    # 소수 판별
    for item in is_prime_num:
        if item.isdigit():
            if isprime(int(item)):
                prime_cnt += 1 
    return prime_cnt