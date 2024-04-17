def close_div(i, j, place):
    if j+1 < 5 and place[i][j+1] == 'P':
        return True
    elif i+1 < 5 and place[i+1][j] == 'P':
        return True
    elif j+1 < 5 and i+1 < 5 and place[i+1][j+1] == 'P':
        if not(place[i+1][j] == 'X' and place[i][j+1] == 'X'):
            return True
    elif i+1 < 5 and j > 0 and place[i+1][j-1] == 'P':
        if not(place[i+1][j] == 'X' and place[i][j-1] == 'X'):
            return True
    elif i+2 < 5 and place[i+2][j] == 'P' and place[i+1][j] != 'X':
        return True
    elif j+2 < 5 and place[i][j+2] == 'P' and place[i][j+1] != 'X':
        return True
    else:
        return False

def solution(places):
    answer = []
    
    for place in places:
        seat_check = 1
        
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    try:
                        if close_div(i,j,place):
                            seat_check = 0
                            break
                    except:
                        pass
            if seat_check == 0:
                break
            
        answer.append(seat_check)
        
    return answer