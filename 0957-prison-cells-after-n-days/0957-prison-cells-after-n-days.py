class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # Time Complexity: O(n)
        # to keep of repeated patterns (for large number)
        memo = {}
        while N:
            if str(cells) in memo:
                N %= memo[str(cells)] - N
            memo[str(cells)] = N
            if N > 0:
                temp = [0] * 8 
                for i in range(1,7):
                    if cells[i-1] == cells[i+1]:
                        temp[i] = 1
                    else:
                        temp[i] = 0
                cells = temp
                N -= 1
        
        return cells
