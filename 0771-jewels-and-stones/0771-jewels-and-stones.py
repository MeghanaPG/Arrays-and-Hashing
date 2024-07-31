class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jwlSet = set(jewels)
        return sum(s in jwlSet for s in stones)
