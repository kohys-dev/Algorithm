import re

def solution(new_id):
    st = new_id

    st = new_id.lower()
    st = re.sub('[^\w._-]', '', st)
    st = re.sub('[.]+', '.', st)
    st = st.strip('.')
    if not st:
        st += 'a'
    if len(st) >= 16:
        st = st[:15].strip('.')

    if len(st) <= 2:
        while True:
            st = st + st[-1]
            if len(st) == 3:
                break

    answer = st
    return answer