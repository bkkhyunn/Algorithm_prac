# Fractional Knapsack problem
# 물건을 쪼갤 수 있는 배낭 문제. 가치가 높은 순으로 정렬한 뒤 배낭에 담고, 남은 부분은 물건을 쪼개어 넣어 조합을 찾는다.
# 대표적인 그리디 알고리즘으로 해결할 수 있는 문제이다.
# 만일 물건을 쪼갤 수 없는 Knapsack problem 은 DP 를 사용해서 해결 가능하다.

# 이익, 무게
cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]


def fractional_knapsack(cargo):
    capacity = 15
    pack = []
    # 단가(이익 / 무게) 계산 역순 정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    # 단가 순 그리디계산
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        # 가방의 용량을 넘어서는 경우, 가방의 남은 용량만큼만 짐을 넣는다.
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break

    return total_value


r = fractional_knapsack(cargo)
print(r)