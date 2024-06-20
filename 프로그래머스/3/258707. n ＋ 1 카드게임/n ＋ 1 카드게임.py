from collections import deque
from itertools import combinations

def solution(coin, cards):
    answer = 0
    n = len(cards)
    deck = cards[:n//3]
    cards = deque(cards[n//3:])
    
    def dfs(deck, cards, coin, r):
        nonlocal n, answer
        
        answer = max(answer, r)
        
        if (len(deck) < 2 and coin <= 0) or len(cards) < 2:
            return answer
        
        # 새로 뽑을 카드 
        new = [cards.popleft() for _ in range(2)]
        
        # 지금 가지고 있는 덱에서 판단
        can_make = False
        for comb in combinations(range(len(deck)), 2):
            if deck[comb[0]] + deck[comb[1]] == n+1:
                can_make = True
                deck.pop(comb[0])
                deck.pop(comb[1])
                break
        
        if can_make:
            # 뽑은 카드는 버리고 현재 있는 카드로만 두 장 내기
            dfs(deck, cards, coin, r+1)
        
            if coin-1 > 0:
                # 하나만 가지는 경우
                dfs(deck+[new[0]], cards, coin-1, r+1)
                dfs(deck+[new[1]], cards, coin-1, r+1)
                
            elif coin-2 > 0:
                # 두개 다 가지는 경우
                dfs(deck+new, cards, coin-2, r+1)
        
        else:
            # 새로 뽑은 카드를 이용해야 두 장 낼 수 있는 상황
            new_deck = deck + new
            can_new_make = False

            for comb in combinations(range(len(new_deck)), 2):
                if new_deck[comb[0]] + new_deck[comb[1]] == n+1:
                    can_new_make = True
                    new_deck.pop(comb[0])
                    new_deck.pop(comb[1])
                    break

            if not can_new_make:
                return r

            else:

                if coin >= 2:
                    # 두개 다 가지는 경우
                    dfs(new_deck, cards, coin-2, r+1)
                    # 하나만 가지는 경우
                    if (n+1 - new[0]) in deck:
                        dfs(deck+[new[0]], cards, coin-1, r+1)
                    elif (n+1 - new[1]) in deck:
                        dfs(deck+[new[1]], cards, coin-1, r+1)
                        
                elif coin == 1:
                    # 하나만 가지는 경우
                    if (n+1 - new[0]) in deck:
                        dfs(deck+[new[0]], cards, coin-1, r+1)
                    elif (n+1 - new[1]) in deck:
                        dfs(deck+[new[1]], cards, coin-1, r+1)

                        
                if coin-2 > 0:
                    # 두개 다 가지는 경우
                    dfs(deck+new, cards, coin-2, r+1)
                    
    return answer

def solution(coin, cards):
    answer = 1

    n = len(cards)
    init_cards_set = set(cards[:len(cards)//3])
    left_cards = cards[len(cards)//3:][::-1] # [::-1]으로 뒤집어서 stack연산 pop()을 사용할거임.
    picked_cards_set = set()

    while True:

        # 남은 카드가 2개 이하인 경우
        if len(left_cards) == 0:
            break # 게임 종료

        # 카드 두 장 뽑기
        picked_cards_set.add(left_cards.pop())
        picked_cards_set.add(left_cards.pop())

        # 원본 카드셋에서 n + 1 조합 만들기.
        is_find = False
        for i in list(init_cards_set):
            other = (n + 1) - i # 기대하는 카드

            if other in init_cards_set and i != other: # 놀랍게도 가능한 조합을 찾음.
                init_cards_set.remove(i)
                init_cards_set.remove(other)

                answer += 1
                is_find = True
                break

        if is_find: 
            continue
        is_find = False

        # 코인이 1개 있는 경우, 초기 카드셋에서 하나, 뽑은 카드셋에서 하나
        if coin >= 1 and init_cards_set and picked_cards_set:
            for i in list(init_cards_set):
                other = (n + 1) - i # 기대하는 카드

                if other in picked_cards_set: # 가능한 조합 Find!
                    init_cards_set.remove(i)
                    picked_cards_set.remove(other)

                    answer += 1
                    coin -= 1
                    is_find = True
                    break

        if is_find: 
            continue
        is_find = False

        # 코인이 2개 있는 경우, 뽑은 카드셋에서 두 개
        if coin >= 2 and len(picked_cards_set) >= 2:
            for i in list(picked_cards_set):
                other = (n + 1) - i # 기대하는 카드

                if other in picked_cards_set and i != other: # 놀랍게도 가능한 조합을 찾음.
                    picked_cards_set.remove(i)
                    picked_cards_set.remove(other)

                    answer += 1
                    coin -= 2
                    is_find = True
                    break

        if is_find:
            continue

        # 아무런 조건에도 해당되지 않은 경우
        break # 게임 종료

    return answer