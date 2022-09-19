def solution(survey, choices):
    scores = {1: -3, 2:-2, 3:-1, 4:0, 5:1, 6:2, 7:3}
    character = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    c_set = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    p_ch = []
    
    for c, s in zip(choices, survey):
        q_score = scores[c]
        if q_score < 0:
            character[s[0]] += abs(q_score)
        elif q_score > 0:
            character[s[1]] += abs(q_score)
            
    for cs in c_set:
        a = character[cs[0]]
        b = character[cs[1]]
        if a == b:
            p_ch.append(min(cs[0], cs[1]))
        elif a < b : 
            p_ch.append(cs[1])
        else:
            p_ch.append(cs[0])
            
    answer = ''.join(p_ch)
    return answer