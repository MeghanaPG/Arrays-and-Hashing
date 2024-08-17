class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Time Complexity: O(n)
        d, ans = defaultdict(int), 0 
        for a, b in dominoes:
            key = min(a,b), max(a,b)
            ans += d[key]
            d[key] += 1
        return ans 
                
            