from collections import defaultdict

class Cell:
    def __init__(self, r, c):
        self.loc = (r, c)
        self.value = "EMPTY"
        self.merged = False
        self.root = (r, c)
        self.child = set()
        
def solution(commands):
    answer = []
    table = [[Cell(i, j) for j in range(51)] for i in range(51)]
    value_dict = defaultdict(set)
    
    for command in commands:
        info = command.split()
        
        if info[0] == "UPDATE":
            
            if len(info) == 4:
                r, c, value = int(info[1]), int(info[2]), info[3]
                
                if table[r][c].merged:
                    rr, rc = table[r][c].root
                    
                    if table[rr][rc].value != "EMPTY":
                        value_dict[table[rr][rc].value].remove((rr, rc))
                        
                    table[rr][rc].value = value
                    value_dict[value].add((rr, rc))
                    
                    for cell in table[rr][rc].child:
                        if cell.value != "EMPTY":
                            value_dict[cell.value].remove(cell.loc)
                        cell.value = value
                        value_dict[value].add(cell.loc)
                        
                if table[r][c].value != "EMPTY":
                    value_dict[table[r][c].value].remove((r, c))
                    
                table[r][c].value = value
                value_dict[value].add((r, c))
                
            else:
                value1, value2 = info[1:]
                if value1 == value2:
                    continue
                    
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
            
            r1, c1 = table[r1][c1].root
            r2, c2 = table[r2][c2].root
                
            if (r1, c1) == (r2, c2):
                continue
            
            table[r1][c1].merged = True
            table[r2][c2].merged = True
            table[r2][c2].root = table[r1][c1].root
            table[r1][c1].child.add(table[r2][c2])
            
            if table[r2][c2].child:
                for cell in table[r2][c2].child:
                    cell.root = (r1, c1)
                    table[r1][c1].child.add(cell)
            
            if value1 == value2:
                table[r2][c2].child = set()
                continue
            
            if value1 == "EMPTY" and value2 == "EMPTY":
                table[r2][c2].child = set()
                continue
                
            elif value1 != "EMPTY" and value2 == "EMPTY":
                table[r2][c2].value = value1
                value_dict[value1].add((r2, c2))
                
                for cell in table[r2][c2].child:
                    cell.value = value1
                    value_dict[value1].add(cell.loc)
                    
            elif value1 == "EMPTY" and value2 != "EMPTY":
                table[r1][c1].value = value2
                value_dict[value2].add((r1, c1))
                
                for cell in table[r1][c1].child:
                    cell.value = value2
                    value_dict[value2].add(cell.loc)
                    
            else:
                value_dict[value2].remove((r2, c2))
                table[r2][c2].value = value1
                value_dict[value1].add((r2, c2))
                for cell in table[r2][c2].child:
                    value_dict[value2].remove(cell.loc)
                    cell.value = value1
                    value_dict[value1].add(cell.loc)
            
            table[r2][c2].child = set()
                
        elif info[0] == "UNMERGE":
            r, c = map(int, info[1:])
            value = table[r][c].value
            
            rr, rc = table[r][c].root
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

            table[rr][rc].child = set()
            
            table[r][c].value = value
            value_dict[value].add((r,c))
            
        else:
            r, c = map(int, info[1:])
            answer.append(table[r][c].value)
        
    return answer