class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_chars = {}
        invalid_upper_chars = set()
        special = 0
        
        for i, char in enumerate(word):
            if char.islower():
                lower_chars[char] = i
        
        for i, char in enumerate(word):
            if char.isupper():
                if char not in invalid_upper_chars and i > lower_chars.get(char.lower(), len(word)):
                    if char.lower() in lower_chars:
                        invalid_upper_chars.add(char)
                        special += 1
                else:
                    invalid_upper_chars.add(char)
            
        return special