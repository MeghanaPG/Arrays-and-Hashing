class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special_characters = set()

        for char in word:
            if char.isalpha():  # Check if it's an alphabetic character
                if char.lower() in word and char.upper() in word:
                    special_characters.add(char.lower())  # Add lowercase to set

        return len(special_characters)