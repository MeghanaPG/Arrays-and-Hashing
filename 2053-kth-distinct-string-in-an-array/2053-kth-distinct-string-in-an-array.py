class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Time and Space: O(n)
        # HashSet 
        distinct_strs = set()
        duplicate_strs = set()

        for s in arr:
            if s in duplicate_strs:
                continue 
            
            if s in distinct_strs:
                distinct_strs.remove(s)
                duplicate_strs.add(s)
            else:
                distinct_strs.add(s)

        # to find the kth distinct
        for s in arr:
            if s not in duplicate_strs:
                k -= 1
            
            if k == 0:
                return s 
        return ""