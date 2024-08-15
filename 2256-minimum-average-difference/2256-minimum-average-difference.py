class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # Time Complexity: o(n^2)
        n = len(nums)

        left, right = 0, sum(nums)

        res, index = float('inf'), 0 

        for i in range(n):
            left += nums[i]
            right -= nums[i]

            #bcz 0 indexed 
            leftAvg = left // (i+1) 
            # it calculates the average of the elements to the right of i. If you are at the last index, it sets the average to 0 because there are no elements to the right.
            rightAvg = right // (n - i - 1) if n - 1 != i else 0 

            if res > abs(leftAvg - rightAvg):
                res = abs(leftAvg - rightAvg)
                index = i

        return index 