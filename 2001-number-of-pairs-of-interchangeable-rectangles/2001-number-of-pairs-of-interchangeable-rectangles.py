class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        myHash = defaultdict(int)
        res = 0 

        for a, b in rectangles:
            ratio = a / b 
            res += myHash[ratio]
            myHash[ratio] += 1

        return res