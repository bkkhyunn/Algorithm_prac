# 화폐 단위를 보고, 큰 단위가 작은 단위의 배수일 때 그리디 알고리즘의 정당성이 확보됨을 파악한다.
# 큰 화폐 단위를 쓰면, 작은 단위의 화폐를 여러 개 쓴 것과 같기 때문에, 큰 화폐 단위부터 사용할 수 있을 만큼 사용하면 최소의 화폐를 사용하는 것이기 때문이다.

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)