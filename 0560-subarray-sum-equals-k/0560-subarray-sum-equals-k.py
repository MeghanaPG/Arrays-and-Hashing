class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize hashmap to store cumulative sum frequencies
        cum_sum_freq = {0: 1}  # to handle the case where subarray starts from index 0
        cum_sum = 0
        count = 0
        
        for num in nums:
            cum_sum += num
            
            # Check if there is a subarray that sums up to k
            if cum_sum - k in cum_sum_freq:
                count += cum_sum_freq[cum_sum - k]
            
            # Update the frequency of the current cumulative sum
            if cum_sum in cum_sum_freq:
                cum_sum_freq[cum_sum] += 1
            else:
                cum_sum_freq[cum_sum] = 1
                
        return count