class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ""
        for ch in s:
            num_str += str(ord(ch) - ord("a") + 1)


        for _ in range(k):
            digit_sum = 0 
            for digit in num_str:
                digit_sum += int(digit)
            if digit_sum < 10:
                return digit_sum
            num_str = str(digit_sum)
        
        return int(num_str)