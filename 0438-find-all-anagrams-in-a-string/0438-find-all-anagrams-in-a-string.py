class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Time Complexity: O(n)

        sorted_p = ''.join(sorted(p))
        res = []

        len_p = len(p)

        for i in range(len(s) + 1 - len(p)):
            window = s[i: i + len_p]

            if ''.join(sorted(window)) == sorted_p:
                res.append(i)
        
        return res