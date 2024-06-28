class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {} #Diff | Index
        for i,n in enumerate(nums):
            diff = target -n
            if diff in mapper:
                return [ i, mapper[diff]]
            mapper[n] = i
        return []
        
        
        