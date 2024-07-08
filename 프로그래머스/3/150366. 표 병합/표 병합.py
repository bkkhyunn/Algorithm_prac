from collections import defaultdict

# 셀 한 칸을 클래스 인스턴스로 만들기
class Cell:
    def __init__(self, r, c):
        
        self.loc = (r, c) # 셀 위치
        self.value = "EMPTY" # 셀 기본 값(빈칸)
        self.merged = False # 셀 병합 유무
        self.root = (r, c) # 셀 병합 시 루트 셀. default 는 자기 자신
        self.child = set() # 셀 병합 시 해당 셀이 루트일 때, 자식 셀을 담는 집합
        
def solution(commands):
    answer = []
    # 엑셀과 비슷한 표 만들기
    table = [[Cell(i, j) for j in range(51)] for i in range(51)]
    # value 업데이트를 위한 value_dict
    value_dict = defaultdict(set)
    
    for command in commands:
        info = command.split()
        
        if info[0] == "UPDATE":
            
            if len(info) == 4:
                r, c, value = int(info[1]), int(info[2]), info[3]
                
                # (r, c) 위치가 병합되어 있는 경우
                if table[r][c].merged:
                    rr, rc = table[r][c].root # 루트 셀 찾기
                    
                    # 루트 셀 값 변경 전, value_dict 의 원래 값에서 해당 위치 제거
                    if table[rr][rc].value != "EMPTY":
                        value_dict[table[rr][rc].value].remove((rr, rc))
                    
                    # 값 업데이트 및 value_dict 최신화
                    table[rr][rc].value = value
                    value_dict[value].add((rr, rc))
                    
                    # 자식 셀 동일한 과정
                    for cell in table[rr][rc].child:
                        if cell.value != "EMPTY":
                            value_dict[cell.value].remove(cell.loc)
                        cell.value = value
                        value_dict[value].add(cell.loc)
                
                # 병합하지 않은 경우
                if table[r][c].value != "EMPTY":
                    value_dict[table[r][c].value].remove((r, c))
                    
                table[r][c].value = value
                value_dict[value].add((r, c))
                
            else:
                value1, value2 = info[1:]
                # 값이 같으면 넘어가기
                if value1 == value2:
                    continue
                
                # value 사전에서 value1 을 없애고, value2 로 갱신
                for (r, c) in list(value_dict[value1]):
                    if value1 != "EMPTY":
                        value_dict[value1].remove((r, c))
                    table[r][c].value = value2
                    value_dict[value2].add((r, c))
                
        elif info[0] == "MERGE":
            r1, c1, r2, c2 = map(int, info[1:])
            
            if (r1, c1) == (r2, c2):
                continue
                
            value1, value2 = table[r1][c1].value, table[r2][c2].value
            
            # 두 셀의 루트 노드 찾기. 병합이 안되어 있으면 자기 자신
            r1, c1 = table[r1][c1].root
            r2, c2 = table[r2][c2].root
            
            # 루트가 같으면 넘어간다.
            if (r1, c1) == (r2, c2):
                continue
            
            table[r1][c1].merged = True
            table[r2][c2].merged = True
            table[r2][c2].root = table[r1][c1].root # 루트 갱신
            table[r1][c1].child.add(table[r2][c2])
            
            # (r2, c2) 의 자식들의 루트도 (r1, c1)으로 변경
            if table[r2][c2].child:
                for cell in table[r2][c2].child:
                    cell.root = (r1, c1)
                    table[r1][c1].child.add(cell)
            
            # 병합할 셀의 값이 같으면 (r2, c2)의 자식들만 초기화 시키고 넘어간다.
            if value1 == value2:
                table[r2][c2].child = set()
                continue
            
            # 병합할 셀의 값이 EMPTY면 (r2, c2)의 자식들만 초기화 시키고 넘어간다.
            if value1 == "EMPTY" and value2 == "EMPTY":
                table[r2][c2].child = set()
                continue
            
            # (r1, c1) 에만 값이 있으면, 기존 (r2, c2) 패밀리의 값을 변경
            elif value1 != "EMPTY" and value2 == "EMPTY":
                table[r2][c2].value = value1
                value_dict[value1].add((r2, c2))
                
                for cell in table[r2][c2].child:
                    cell.value = value1
                    value_dict[value1].add(cell.loc)
            
            # (r2, c2) 에만 값이 있으면, 기존 (r1, c1) 패밀리의 값을 변경
            elif value1 == "EMPTY" and value2 != "EMPTY":
                table[r1][c1].value = value2
                value_dict[value2].add((r1, c1))
                
                for cell in table[r1][c1].child:
                    cell.value = value2
                    value_dict[value2].add(cell.loc)
            
            # 두 셀 모두 값이 있을 경우 (r2, c2) 패밀리의 값을 (r1, c1) 의 값으로 변경
            else:
                value_dict[value2].remove((r2, c2))
                table[r2][c2].value = value1
                value_dict[value1].add((r2, c2))
                
                for cell in table[r2][c2].child:
                    value_dict[value2].remove(cell.loc)
                    cell.value = value1
                    value_dict[value1].add(cell.loc)
            
            # 값을 모두 변경했으면, 병합된 (r2, c2) 패밀리의 자식값을 초기화
            table[r2][c2].child = set()
                
        elif info[0] == "UNMERGE":
            r, c = map(int, info[1:])
            value = table[r][c].value
            
            rr, rc = table[r][c].root # 루트부터 차례대로 병합 해제
            table[rr][rc].merged = False
            
            if table[rr][rc].value != "EMPTY":
                value_dict[table[rr][rc].value].remove((rr, rc))
                table[rr][rc].value = "EMPTY"
            
            for cell in table[rr][rc].child:
                if cell.value != "EMPTY":
                    value_dict[cell.value].remove(cell.loc)
                    cell.value = "EMPTY"
                cell.merged = False
                cell.root = cell.loc
            
            # 루트의 자식 초기화
            table[rr][rc].child = set()
            
            table[r][c].value = value
            value_dict[value].add((r,c))
            
        else:
            r, c = map(int, info[1:])
            answer.append(table[r][c].value)
        
    return answer