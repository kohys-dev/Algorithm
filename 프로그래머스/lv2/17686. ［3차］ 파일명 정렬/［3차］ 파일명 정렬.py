import re 

def solution(files):
    text = [re.split(r'([0-9]+)', f) for f in files]
    filename_sorted = sorted(text, key = lambda x:(x[0].lower(), int(x[1])))
    answer = [''.join(file) for file in filename_sorted]
    return answer