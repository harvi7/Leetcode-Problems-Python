class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextDay(cells):
            tmp = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    tmp[i] = 1
                    
            return ''.join(map(str, tmp))
            
        if not cells or len(cells) == 0 or N <= 0:
            return cells
        hasCycle = False
        cycle = 0
        cycle_set = [] 
        for i in range(N):
            next_cycle = nextDay(cells)
            if next_cycle not in cycle_set:
                cycle_set.append(next_cycle)
                cycle += 1
            
            else:
                hasCycle = True
                break
            
            cells = next_cycle
        
        if hasCycle:
            N = N % cycle;
            for i in range(N):
                cells = nextDay(cells)
       
        return cells
    
    