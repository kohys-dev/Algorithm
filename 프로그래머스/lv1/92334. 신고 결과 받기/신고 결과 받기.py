from collections import Counter
import numpy as np


def solution(id_list, report, k):
    answer = []
    reporter = []
    repondent_list = []
    user_report = {}
    stopped_id = []
    rmdu_report = list(set(report))

    for item in rmdu_report:
        reporter = item.split()[0]
        repondent = item.split()[1]
        repondent_list.append(repondent)
        if reporter in user_report:
            pass
        else:
            user_report[reporter] = [] 
        
        user_report[reporter].append(repondent)
            
    for key, value in dict(Counter(repondent_list)).items():
        if value >= k:
            stopped_id.append(key)
            
    for item in id_list:
        mailing_cnt = 0
        try:
            for sid in stopped_id:
                if sid in user_report[item]:
                    mailing_cnt += 1
        except:
            pass
        answer.append(mailing_cnt)
        
    return answer