class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Time: O(n)
        counter = Counter(nums)
        ans = 0 
        for c in counter.values():
            if c == 1:
                return -1
            ans += ceil(c/3)
        return ans

        
            

