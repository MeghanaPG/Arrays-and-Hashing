class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        # Time Complexity: O(n)

        min_num = min(nums)
    
        numSum = sum(int(digit) for digit in str(min_num))

        return 0 if numSum % 2 != 0 else 1