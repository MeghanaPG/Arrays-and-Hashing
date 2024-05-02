from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert numbers to strings and define custom sorting function
        nums = sorted(map(str, nums), key=lambda x: x*10, reverse=True)
        
        # Handle the case where all numbers are 0
        if nums[0] == '0':
            return '0'
        
        # Concatenate the sorted strings to form the largest number
        return ''.join(nums)

