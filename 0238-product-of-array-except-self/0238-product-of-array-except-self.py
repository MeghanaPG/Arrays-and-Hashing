class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix_arr = [1] * len(nums)
        postfix_arr = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_arr[i] = prefix_arr[i-1] * nums[i-1]

        
        for i in range(len(nums)-2, -1, -1):
            postfix_arr[i] = postfix_arr[i+1] * nums[i+1]
        

        for i in range(len(nums)):
            res[i] = prefix_arr[i] * postfix_arr[i]
        
        return res