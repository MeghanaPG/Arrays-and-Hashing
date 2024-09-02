class Solution:
    def partitionString(self, s: str) -> int:
        # Time Complexity: O(n)
        # Memory: O(26) -> O(1)
        curSet = set()
        # res is 1 as we are going to have a non empty s to begin with
        res = 1

        for c in s:
            if c in curSet:
                res += 1
                # reset
                curSet = set()
            curSet.add(c)
        return res 