from collections import deque

def solution(coin, cards):
    answer = 1

    n = len(cards)
    init_cards_set = set(cards[:n//3])
    left_cards = deque(cards[n//3:])
    # 뽑은 카드는 나중에 써도 최대 라운드 결과는 달라지지 않는다. 숫자들 간의 중복이 없기 때문이다.
    picked_cards_set = set()

    while True:

        # 남은 카드가 2개 이하인 경우
        if len(left_cards) == 0:
            break # 게임 종료

        # 카드 두 장 뽑기
        picked_cards_set.add(left_cards.popleft())
        picked_cards_set.add(left_cards.popleft())

        # 뽑은 카드를 사용 안 하는 경우
        can_make = False
        for i in list(init_cards_set):
            # n + 1 이 되기 위해 필요한 카드
            expect = (n + 1) - i
            
            # 가지고 있는 카드에서 해결
            if expect in init_cards_set:
                init_cards_set.remove(i)
                init_cards_set.remove(expect)

                answer += 1
                can_make = True
                break

        if can_make: 
            continue
            
        can_make = False

        # 코인이 1개 이상 있는 경우, 초기 카드셋에서 하나, 뽑은 카드셋에서 하나
        if coin >= 1 and init_cards_set and picked_cards_set:
            for i in list(init_cards_set):
                # n + 1 이 되기 위해 필요한 카드
                expect = (n + 1) - i

                if expect in picked_cards_set and i != expect:
                    init_cards_set.remove(i)
                    picked_cards_set.remove(expect)

                    answer += 1
                    coin -= 1
                    can_make = True
                    break

        if can_make: 
            continue
        can_make = False

        # 코인이 2개 이상 있는 경우, 뽑은 카드셋에서 두 개
        if coin >= 2 and len(picked_cards_set) >= 2:
            for i in list(picked_cards_set):
                # n + 1 이 되기 위해 필요한 카드
                expect = (n + 1) - i

                if expect in picked_cards_set and i != expect:
                    picked_cards_set.remove(i)
                    picked_cards_set.remove(expect)

                    answer += 1
                    coin -= 2
                    can_make = True
                    break

        if can_make:
            continue

        # 아무런 조건에도 해당되지 않은 경우
        break # 게임 종료

    return answer