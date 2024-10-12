class Solution(object):
    def twoSum(self, nums, target):
        my_hash = {}
        
        for i, n in enumerate(nums):
            complement = target - n 

            if complement in my_hash:
                return [my_hash[complement], i]
            
            my_hash[n] = i 
        
        return None


    
        
        
                

        