class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_dict_s = {}
        count_dict_t = {}

        for c in s:
            if c in count_dict_s:
                count_dict_s[c] += 1
            else:
                count_dict_s[c] = 1 
            
        
        for ch in t:
            if ch in count_dict_t:
                count_dict_t[ch] += 1
            else:
                count_dict_t[ch] = 1 
            
        
        return count_dict_s == count_dict_t