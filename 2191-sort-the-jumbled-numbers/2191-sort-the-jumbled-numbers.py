class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        store_pairs = []

        for i in range(len(nums)):
            number = str(nums[i])
            formed = ""
            for j in range(len(number)):
                formed = formed + str(mapping[int(number[j])])
            # store the mapped value 
            mapped_value = int(formed)
            store_pairs.append((mapped_value, i))
        
        store_pairs.sort()
        answer = []
        for pair in store_pairs:
            answer.append(nums[pair[1]])
        return answer
