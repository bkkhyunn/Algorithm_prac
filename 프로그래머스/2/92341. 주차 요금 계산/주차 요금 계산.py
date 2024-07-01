from itertools import zip_longest
import math

def solution(fees, records):
    answer = []
    
    # 차량 번호 별 IN, OUT 시간 담기
    cars = set([record.split()[1] for record in records])
    park_dict = {car:[[],[]] for car in cars}
    
    for record in records:
        t, num, info = record.split()
        if info == 'IN':
            park_dict[num][0].append(t)
        else:
            park_dict[num][1].append(t)
    
    # 차량 번호가 적은 것부터
    for num in sorted(park_dict.keys()):
        # 누적 주차 시간
        park_time = 0
        for in_info, out_info in zip_longest(park_dict[num][0], park_dict[num][1],
                                             fillvalue="23:59"):
            ih = (int(in_info.split(':')[0])*60) + int(in_info.split(':')[1])
            oh = (int(out_info.split(':')[0])*60) + int(out_info.split(':')[1])
            park_time += (oh - ih)
        
        if park_time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((park_time - fees[0]) / fees[2]) * fees[3]))
        
    return answer