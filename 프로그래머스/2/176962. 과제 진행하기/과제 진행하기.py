def solution(plans):
    for p in plans:
        p[1] = (int(p[1].split(':')[0]) * 60) + int(p[1].split(':')[1])
        p[2] = int(p[2])
    plans.sort(key=lambda x: x[1])
    complete, temp = [], []
    s = 0
    t = plans[s][1]
    while len(complete) != len(plans):
        if s == len(plans) - 1:
            complete.append(plans[s][0])
            for t, _ in temp[::-1]:
                complete.append(t)
        else:
            n, l = plans[s][0], plans[s][2]
            if t+l > plans[s+1][1]:
                temp.append([n, l-(plans[s+1][1]-t)])
                t = plans[s+1][1]
            elif t+l == plans[s+1][1]:
                complete.append(n)
                t = plans[s+1][1]
            elif t+l < plans[s+1][1]:
                complete.append(n)
                t = t+l
                extra = plans[s+1][1] - t
                while temp and extra != 0:
                    if temp[-1][1] <= extra:
                        extra -= temp[-1][1]
                        complete.append(temp.pop()[0])
                    else:
                        temp[-1][1] -= extra
                        extra = 0
                t = plans[s+1][1]
        s += 1
            
    return complete