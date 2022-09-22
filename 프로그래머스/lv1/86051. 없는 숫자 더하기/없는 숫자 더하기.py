def solution(numbers):
    num_list = set([i for i in range(0, 10)])
    set_numbers = set(numbers)
    
    return sum(list(num_list-set_numbers))