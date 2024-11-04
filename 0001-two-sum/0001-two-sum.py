class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)

        # Loop through the array
        for i in range(l):
            for j in range(i + 1, l):  # Start j from i + 1 to avoid using the same element
                sum_pair = nums[i] + nums[j]  # Sum the two elements
                if sum_pair == target:
                    return [i, j]  # Return the indices if they add up to target

        # If no solution is found, raise an error or return an empty list
        raise ValueError("No two sum solution")