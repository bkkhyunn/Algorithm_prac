def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    start_sec = h1 * 3600 + m1 * 60 + s1
    end_sec = h2 * 3600 + m2 * 60 + s2

    if start_sec == 0 or start_sec == 12 * 3600:
        answer += 1
        

    while start_sec < end_sec:
        
        # 초당 각도 이동 -> 시침: 1/120, 분침: 1/10, 초침: 6
        h_angle = start_sec / 120 % 360
        m_angle = start_sec / 10 % 360
        s_angle = start_sec * 6 % 360
        
        new_h_angle = 360 if (start_sec+1) / 120 % 360 == 0 else (start_sec+1) / 120 % 360
        new_m_angle = 360 if (start_sec+1) / 10 % 360 == 0 else (start_sec+1) / 10 % 360
        new_s_angle = 360 if (start_sec+1) * 6 % 360 == 0 else (start_sec+1) * 6 % 360
        
        if s_angle < h_angle and new_s_angle >= new_h_angle:
            answer += 1
        
        if s_angle < m_angle and new_s_angle >= new_m_angle:
            answer += 1
        
        if new_s_angle == new_h_angle and new_h_angle == new_m_angle:
            answer -= 1
        
        start_sec += 1
        
    return answer