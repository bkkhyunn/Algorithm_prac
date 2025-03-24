from itertools import permutations, combinations, product

N = 10
M = 3

# 1 ~ N 사이의 값 중에 M개 뽑기 - 순열
number = [i for i in range(1, N+1)]
for perm in permutations(number, M):
    print(perm)

# 1 ~ N 사이 값 중에 M개 뽑기 - 조합. 같은 것들의 순서를 고려하지 않음
number = [i for i in range(1, N+1)]
for comb in combinations(number, M):
    print(comb)

# 1 ~ N 사이 값을 M 개 미만의 부분집합 뽑기 - 중복 순열
number = [i for i in range(1, N+1)]
for i in range(1, M+1):
	for prd in product(number, repeat=i):
		print(prd)