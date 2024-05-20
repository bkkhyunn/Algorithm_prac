def solution(land):
    
    n, m = len(land), len(land[0])
    
    def dfs(coord):
        nonlocal oil, land, coords
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        stack = [coord]
        while stack:
            x, y = stack.pop()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >=n or ny>=m:
                    continue

                if land[nx][ny]:
                    land[nx][ny] = 0
                    oil += 1
                    coords.add(ny)
                    stack.append((nx, ny))
    
    discovered = {c:0 for c in range(m)}
    for j in range(m):
        oil = 0
        coords = set()
        for i in range(n):
            if land[i][j]:
                land[i][j] = 0
                coord = (i, j)
                coords.add(j)
                oil += 1
                #print(i, j, oil)
                dfs(coord)
            for c in coords:
                discovered[c] += oil
            coords = set()
            oil = 0
        #print(discovered)
    return max(discovered.values())