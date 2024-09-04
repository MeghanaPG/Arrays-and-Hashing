class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # Time Complexity: O(n)
        # for each ratio we will store it's count
        myHash = defaultdict(int)
        res = 0 

        for w,h in rectangles:
            ratio = w/h
            res += myHash[ratio]
            myHash[ratio] += 1
        return res 