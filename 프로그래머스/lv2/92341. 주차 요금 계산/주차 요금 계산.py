from datetime import datetime
import math

def get_interval(parkin, parkout):
    park_in = datetime.strptime(parkin, '%H:%M')
    park_out = datetime.strptime(parkout, '%H:%M')
    interval = int((park_out - park_in).total_seconds() / 60)   
    return interval

def get_fee(time, fees):
    if time <= fees[0]:
        return fees[1]
    else:
        return fees[1] + (math.ceil((time-fees[0])/fees[2]))*fees[3]

def solution(fees, records):
    parked = {}
    parking_interval = {}
    
    for record in records:
        data = record.split(' ')
        if data[2] == 'IN':
            parked[data[1]] = data[0]
        else:
            interval = get_interval(parked[data[1]], data[0])
            try: parking_interval[data[1]] += interval
            except: parking_interval[data[1]] = interval
            del parked[data[1]]
    
    if parked:
        for car in parked:
            interval_ = get_interval(parked[car], '23:59')
            try: parking_interval[car] += interval_
            except: parking_interval[car] = interval_

    parking_interval = dict(sorted(parking_interval.items(), key=lambda item:item[0]))
    
    answer = []
    for car_ in parking_interval:
        answer.append(get_fee(int(parking_interval[car_]), fees))
        
    return answer
    