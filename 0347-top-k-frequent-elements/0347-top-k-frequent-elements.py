from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1 
            
        counter = Counter(num_freq)
        
        key_value_pairs = counter.most_common(k)
        top_k_elements = [pair[0] for pair in key_value_pairs]
        return top_k_elements
            
            