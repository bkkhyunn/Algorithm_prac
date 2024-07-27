n = int(input())

diagonal = 1 # 대각선 번호
cnt = 1 # 원소 개수

while cnt < n:
    diagonal += 1
    cnt += diagonal

offset = cnt - n # n 번째 원소 위치

if diagonal % 2 == 0:
    r, c = diagonal - offset, offset + 1
else:
    r, c = offset + 1, diagonal - offset
print(f'{r}/{c}')