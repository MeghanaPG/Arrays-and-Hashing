class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        left = [-1] * N  
        right = [-1] * N
        prefix = [0] * N

        # Fill left array with the position of the closest candle to the left or at the current position
        for i in range(N):
            if s[i] == "|":
                left[i] = i
            else:
                if i > 0:
                    left[i] = left[i - 1]
        
        # Fill right array with the position of the closest candle to the right of the current position
        for i in range(N - 1, -1, -1):
            if s[i] == "|":
                right[i] = i
            else:
                if i < N - 1:
                    right[i] = right[i + 1]
        
        # Fill prefix array with cumulative counts of plates
        for i in range(1, N):
            prefix[i] = prefix[i - 1] + (1 if s[i] == "*" else 0)
        
        ans = []
        for l, r in queries:
            r = left[r]
            l = right[l]
            if l == -1 or r == -1 or l > r:
                ans.append(0)
            else:
                ans.append(prefix[r] - prefix[l])
        
        return ans
