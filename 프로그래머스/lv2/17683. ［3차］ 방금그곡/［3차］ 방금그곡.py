from datetime import datetime

def notes_change(n):
    return n.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def solution(m, musicinfos):
    m = notes_change(m)
    answer = []
    
    for i, info in enumerate(musicinfos):
        
        temp = info.split(',')
        temp[3] = notes_change(temp[3])
        s = datetime.strptime(temp[0], '%H:%M')
        e = datetime.strptime(temp[1], '%H:%M')
        pt = int(((e-s).seconds)/60)
        
        notes = (pt//len(temp[3])*temp[3]) + (temp[3][:pt%len(temp[3])+1])
        if m in notes:
            answer.append([temp[2], pt, i])
            
    if not answer:
        return '(None)'
    elif len(answer) > 1:
        answer = sorted(answer, key = lambda x : (-x[1], x[2]))
        print(answer)
    return answer[0][0]     