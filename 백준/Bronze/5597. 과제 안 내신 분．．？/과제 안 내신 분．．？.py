import sys
input = sys.stdin.readline

students = set([i+1 for i in range(30)])

for _ in range(28):
    n = int(input())
    students.remove(n)
students = sorted(list(students))
for i in range(2):
    print(students[i])