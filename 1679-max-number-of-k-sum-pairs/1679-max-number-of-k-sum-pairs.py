class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Time Complexiy: O(nlogn)
        c = Counter(nums)
        output = 0 
        seen = set()

        for x in c:
            if x not in seen and (k-x) in c:
                if x == (k-x):
                    output += c[x]//2
                else:
                    # count 
                    output += min(c[x], c[k-x])
                    seen.add(x)
                    seen.add(k-x)
        return output  

        
        
        
        
        
        
        
        # sorted(nums)
        # res = 0 

        # l = 0 
        # r = len(nums)-1
        # while l < r:
        #     if nums[l] + nums[r] == k:
        #         res += 1 
        #     # l += 1
        #     r -= 1
        # return res
