class Solution:
    def frequencySort(self, s: str) -> str:
        # Time Complexity: O(n)
        freqMap = {}

        for c in s:
            if c in freqMap:
                freqMap[c] += 1
            else:
                freqMap[c] = 1 
            
        
        sorted_char = sorted(freqMap.items(), key = lambda x:x[1], reverse= True)
        
        res = ''.join(char*count for char, count in sorted_char)

        return res 