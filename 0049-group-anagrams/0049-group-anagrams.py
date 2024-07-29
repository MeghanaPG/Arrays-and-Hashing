class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        sorted_str_list = []

        anagram_hashtable = {}

        for each in strs:
            str_list = list(each)
            str_list.sort()
            sorted_str = "".join(str_list)
            sorted_str_list.append(sorted_str)

        
        for i, key in enumerate(sorted_str_list):
            if key in anagram_hashtable:
                anagram_hashtable[key].append(strs[i])
            else:
                anagram_hashtable[key] = [strs[i]]
        
        return list(anagram_hashtable.values())