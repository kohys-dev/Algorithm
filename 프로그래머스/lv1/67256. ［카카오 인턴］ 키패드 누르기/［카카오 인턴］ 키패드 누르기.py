def cal_dist(status_list, coordinate_dict, key):
    x = abs(status_list[-1][0] - coordinate_dict[key][0])
    y = abs(status_list[-1][1] - coordinate_dict[key][1])
    return x+y
                                                      
def solution(numbers, hand):
    num_coordinate = {1:(1,4), 2:(2,4), 3:(3,4), 4:(1,3), 5:(2,3), 6:(3,3), 7:(1,2), 8:(2,2), 9:(3,2), 0:(2,1)}
    answer = ''
    cur_L = [(1,1)]
    cur_R = [(3,1)]
    for item in numbers:
        cur_cor = num_coordinate[item]
        x = num_coordinate[item][0]
        print(item)
        if x == 1:
            answer += 'L'
            cur_L.append(cur_cor)
            
        elif x == 3:
            answer += 'R'
            cur_R.append(cur_cor)
            
        else:
            dist_L = cal_dist(cur_L, num_coordinate, item)
            dist_R = cal_dist(cur_R, num_coordinate, item)
            if dist_L > dist_R:
                answer += 'R'
                cur_R.append(cur_cor)
            elif dist_L < dist_R:
                answer += 'L'
                cur_L.append(cur_cor)
            else:
                k = hand[0]
                if k == 'r':
                    cur_R.append(cur_cor)
                else:
                    cur_L.append(cur_cor)
                answer += k.upper()
    return answer