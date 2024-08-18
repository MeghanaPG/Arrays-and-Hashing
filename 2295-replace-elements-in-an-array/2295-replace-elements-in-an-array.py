class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
    # Time Complexity: O(n+m)
    # Space: O(n)

        myHash = {}
        for i, x in enumerate(nums):
            myHash[x] = i

        for x,y in operations:
            index = myHash[x]

            nums[index] = y 
            myHash[y] = index 
            del myHash[x]
        return nums