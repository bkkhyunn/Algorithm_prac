from itertools import product

def solution(users, emoticons):
    answer = []
    rates = [10, 20, 30, 40]

    discounted = list(product(rates, repeat=len(emoticons)))

    for discount in discounted:
        plus_service = 0
        sale = 0

        for user in users:
            user_rate, user_price = user
            purchased = 0
            
            for i, emo in enumerate(emoticons):
                if user_rate <= discount[i]:
                    # 한 사용자의 구매액은 자신의 기준 할인율 이상 할인하는 이모티콘의 할인가
                    purchased += emo * (100 - discount[i]) // 100
                    
            if purchased >= user_price:
                # 총 구매액이 사용자의 예산 이상이라면, 구매하지 않고 플러스 가입
                plus_service += 1
            else:
                # 그렇지 않다면 이모티콘 구매하므로 총 판매금액에 합산    
                sale += purchased
        # 할인율 조합별 총 가입자수와 판매액을 배열에 저장
        answer.append((plus_service, sale))
    # 조합별 가장 가입자수 > 판매액 순으로 큰 경우를 찾아 리턴
    answer = sorted(answer, reverse=True, key=lambda x: (x[0], x[1]))

    return answer[0]
