# 할인이 4가지만 가능하고, 이모티콘은 최대 7개, 유저는 최대 100명이기 때문에 1억이 넘지 않는다.
# 따라서 완전탐색으로 해결

from itertools import product

def solution(users, emoticons):
    answer = []
    # 할인 가능 비율
    rates = [10, 20, 30, 40]
    
    # 각 이모티콘 별로 할인율 조합
    discounted = list(product(rates, repeat=len(emoticons)))

    for discount in discounted:
        # 플러스 서비스 가입자, 판매액
        plus_service, sale = 0, 0

        for user in users:
            user_rate, user_price = user
            purchased = 0
            
            for i, emo in enumerate(emoticons):
                # 유저 할인율 이상으로 할인 됐을 때
                if user_rate <= discount[i]:
                    # 구매
                    purchased += emo * (100 - discount[i]) // 100
            
            # 구매액이 유저가 설정한 예산 이상이면 플러스 가입
            if purchased >= user_price:
                plus_service += 1
            # 그렇지 않다면 이모티콘 구매
            else:
                sale += purchased
        
        # 할인율 조합별 총 가입자수와 판매액을 배열에 저장
        answer.append((plus_service, sale))
        
    # 조합별 가입자수 - 판매액 순으로 큰 경우를 리턴
    answer = sorted(answer, reverse=True, key=lambda x: (x[0], x[1]))

    return answer[0]