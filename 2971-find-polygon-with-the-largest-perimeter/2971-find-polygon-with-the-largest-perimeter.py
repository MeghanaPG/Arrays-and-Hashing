class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Time Complexity: O(nlogn)
        nums.sort()
        res = -1
        total = 0 

        for n in nums:
            if total > n:
                res = total + n
            total += n 
        return res 