class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        my_dict = {}
        res = []
        n = len(nums)

        if n <= 1:
            return nums

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1 
            else:
                my_dict[num] = 1 
            
        # to check the occurence if it is greater than n/3
        for key, val in my_dict.items():
            if val > n/3:
                res.append(key)
        
        return res

        
