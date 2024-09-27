class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [1] * len(candies)
        greatest_num = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest_num:
                res[i] = True
            else:
                res[i] = False 
        return res 