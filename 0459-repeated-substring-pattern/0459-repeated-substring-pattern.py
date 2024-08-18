class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Time and Space: O(n)
        new_str = s + s 
        if s in new_str[1:-1]:
            return True 
        return False 
