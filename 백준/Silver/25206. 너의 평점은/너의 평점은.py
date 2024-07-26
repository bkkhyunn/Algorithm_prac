score = '''A+	4.5
A0	4.0
B+	3.5
B0	3.0
C+	2.5
C0	2.0
D+	1.5
D0	1.0
F	0.0'''.split()
score = {score[i]:float(score[i+1]) for i in range(0, len(score), 2)}
total_score = 0
total_credit = 0
for _ in range(20):
    name, credit, s = input().split()
    if s == 'P':
        continue
    total_credit += float(credit)
    total_score += (float(credit) * score[s])

print(total_score / total_credit)