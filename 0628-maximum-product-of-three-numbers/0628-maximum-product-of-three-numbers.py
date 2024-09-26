class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Time: O(n)
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1]*nums[-2]*nums[-3])