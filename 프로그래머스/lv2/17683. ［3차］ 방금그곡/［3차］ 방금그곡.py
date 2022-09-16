from datetime import datetime

def solution(m, musicinfos):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    answer = []
    
    for i, info in enumerate(musicinfos):
        
        temp = info.split(',')
        temp[3] = temp[3].replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        s = datetime.strptime(temp[0], '%H:%M')
        e = datetime.strptime(temp[1], '%H:%M')
        pt = int(((e-s).seconds)/60)
        if pt > len(temp[3]):
            if pt%len(temp[3]) != 0:
                cnt = pt//len(temp[3]) + 1
            else:
                cnt = pt//len(temp[3])
            notes = temp[3] * cnt
        elif pt < len(temp[3]):
            notes = temp[3][:pt+1]
        else:
            notes = temp[3]
            
        if m in notes:
            answer.append([temp[2], pt, i])
    if not answer:
        return '(None)'
    elif len(answer) > 1:
        answer = sorted(answer, key = lambda x : (-x[1], x[2]))
        print(answer)
    return answer[0][0]     