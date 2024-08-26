class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Time Complexity: 
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1 

        nums = sorted(nums, key=cmp_to_key(compare))

        # int and str again to handle the leading zeros
        return str(int("".join(nums)))