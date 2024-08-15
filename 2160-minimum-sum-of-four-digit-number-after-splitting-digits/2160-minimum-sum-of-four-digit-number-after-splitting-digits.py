class Solution:
    def minimumSum(self, num: int) -> int:
        # 2932
        # Sort them first 
        # Both the small digits will be the first num and other two will be the next digits resepectively.
        numStr = str(num)
        sorted_digits = sorted(numStr)
        num1 = sorted_digits[0] + sorted_digits[2]
        num2 = sorted_digits[1] + sorted_digits[3]
        res = int(num1) + int(num2)
        return res 