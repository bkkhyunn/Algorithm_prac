# Union Find 로 풀기

def solution(commands):
    answer = []
    table = [i for i in range(51 * 51)]
    values = ["" for _ in range(51 * 51)]
    
    def find(x):
        nonlocal table
        if x != table[x]:
            table[x] = find(table[x]) # 경로 압축
            
        return table[x]

    def union(x1, x2):
        nonlocal table, values
        
        root1 = find(x1)
        root2 = find(x2)

        # (r1, c1) 셀에 값이 없고 (r2, c2)에만 있는 경우
        if not values[root1] and values[root2]:
            table[root1] = root2
            values[root1] = values[root2]
        else:
            table[root2] = root1
            values[root2] = values[root1]
    
    # 명령어 실행
    for command in commands:
        command = command.split()
        
        if command[0] == 'UPDATE':
            
            if len(command) == 4:
                r, c, value = command[1:]
                r, c = int(r), int(c)
                # (r, c)의 루트 셀의 value 만 바꾼다.
                x = r * 50 + c
                root = find(x)
                values[root] = value

            else:
                # value1을 모두 찾아, value2로 바꿔준다.
                value1, value2 = command[1:]
                for i in range(51 * 51):
                    if values[i] == value1:
                        values[i] = value2

        elif command[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, command[1:])

            x1 = r1 * 50 + c1
            x2 = r2 * 50 + c2
            
            # 루트 셀이 다르면 병합한다.
            if table[x1] != table[x2]:
                union(x1, x2)

        elif command[0] == 'UNMERGE':
            r, c = map(int, command[1:])
            x = r * 50 + c
            root = find(x)
            value = values[root]

            cells = []
            for cell in range(51 * 51):
                if find(cell) == root:
                    cells.append(cell)

            for cell in cells:
                values[cell] = ''
                table[cell] = cell

            values[x] = value

        elif command[0] == 'PRINT':
            r, c = map(int, command[1:])
            x = r * 50 + c
            root = find(x)

            if not values[root]:
                answer.append('EMPTY')
            else:
                answer.append(values[root])

    return answer