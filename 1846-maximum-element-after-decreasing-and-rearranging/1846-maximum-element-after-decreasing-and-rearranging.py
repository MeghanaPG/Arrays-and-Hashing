class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # arr = [2,2,1,2,1]
        # arr = [1,3,2,2,2]
        arr.sort()
        ans = 1 

        for i in range(1, len(arr)):
            if arr[i] >= ans + 1:
                ans += 1 
        
        return ans

