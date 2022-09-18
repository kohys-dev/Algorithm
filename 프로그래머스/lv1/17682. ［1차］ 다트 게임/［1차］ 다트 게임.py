import re

def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    dartResult = (re.sub(r'(\d+)?(\w)?(\W?)?',r'\1\2\3 ', dartResult)).split(' ')
    dart_r = [x for x in dartResult if x != '']
    scores = []
    for i, dart in enumerate(dart_r):
        print(dart)
        s = re.sub(r'[^0-9]', '', dart)
        b = re.sub(r'[^a-zA-Z]', '', dart)
        o = re.sub(r'[^\W]', '', dart)
        game_score = int(s) ** bonus[b]
        if o == '*':
            try:
                scores[i-1] = scores[i-1] * 2
                scores.append(game_score * 2)
            except:
                scores.append(game_score * 2)
        elif o == '#':
            scores.append(game_score * (-1))
        else:
            scores.append(game_score)
    
    return sum(scores)