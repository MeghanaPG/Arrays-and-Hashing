class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArray = [0] * (len(nums))
        for i in range(len(nums)):
            newArray[i] = nums[i]
            i += 1
        res = nums + newArray 
        return res 