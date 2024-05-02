class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Time Complexity: O(n)
        countGap = {0:0} #mapping pos to count of brick gaps

        for row in wall:
            total = 0 
            # we don't want to count the gap at the right most position 
            # so we don't have to consider the right most brick
            for b in row[:-1]:
                total += b 
                countGap[total] = 1 + countGap.get(total,0)
                # rows - maxgap = res 
        return len(wall) - max(countGap.values())