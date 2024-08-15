class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # Time Compelexity: O(n)
        myHash = {} 

        for n in nums:
            if n in myHash:
                myHash[n] += 1 
            else:
                myHash[n] = 1 
        
        new_list = [n for n in myHash if myHash[n] == 1]

        if not new_list:
            return -1 
        
        return max(new_list)
     
