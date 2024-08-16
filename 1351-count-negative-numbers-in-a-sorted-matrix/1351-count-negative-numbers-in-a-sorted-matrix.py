class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0 

        for g in grid:
            for n in g:
                if n < 0:
                    count += 1 
        
        return count 