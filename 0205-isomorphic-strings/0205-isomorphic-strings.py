class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time Complexity: O(n)
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s,t):
            # if the mapping is present already then we will return false 
            if((c1 in mapST and mapST[c1] != c2) or
            (c2 in mapTS and mapTS[c2] != c1)):
                return False 
            mapST[c1] = c2 
            mapTS[c2] = c1 

        return True 