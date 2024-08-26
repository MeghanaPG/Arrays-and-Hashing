class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)
        changed = False 

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i+1]:
                continue 
            
            if changed:
                return False 
            
            # we want to decrease left element 
            #     i  i+1
            # [3, 6, 5]  
            if i == 0 or nums[i + 1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
            # [3, 4, 2]
                nums[i + 1] = nums[i]
            changed = True
        return True 
        


                