import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

print(sum([score / max_score * 100 for score in scores]) / n)