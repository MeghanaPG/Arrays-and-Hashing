class Solution:
    def minimumPushes(self, word: str) -> int:
        # Time Complexity: O(n)
        counts = [0] * 26 
        for c in word:
            # a -> x 
            # b -> x + 1 
            # c -> x + 2
            counts[ord(c) - ord("a")] += 1 

        counts.sort(reverse=True)

        res = 0 
        for i, cnt in enumerate(counts):
            res += cnt * (1 + i // 8)
        return res 

