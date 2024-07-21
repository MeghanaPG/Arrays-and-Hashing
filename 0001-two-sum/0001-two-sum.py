class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in myHash:
                return [myHash[complement], i]

            myHash[n] = i
        
        return None 