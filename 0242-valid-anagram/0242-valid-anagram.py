class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_dict_s = {}
        count_dict_t = {}

        for c in s:
            if c not in count_dict_s:
                count_dict_s[c] = 1
            else:
                count_dict_s[c] += 1
            

        for c in t:
            if c not in count_dict_t:
                count_dict_t[c] = 1
            else:
                count_dict_t[c] += 1
        
        return count_dict_s == count_dict_t