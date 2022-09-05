def solution(record):
    uids = {}
    logs = []
    update_code = ['Enter', 'Change']
    status = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
    answer = []
    for item in record:
        s = item.split()
        if s[0] in update_code:
            uids[s[1]] = s[2]

            if s[0] == 'Enter':
                logs.append(s[0] + ' ' + s[1])
        else:
            logs.append(item)

    for log in logs:
        log = log.split()
        answer.append(uids[log[1]] + '님이 ' + status[log[0]])

    return answer