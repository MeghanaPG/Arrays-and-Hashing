class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # Time and Space: O(n), O(1)
        best = 10 ** 10
        besti = -1

        for index, (x1,y1) in enumerate(points):
            if x == x1 or y == y1:
                dist = abs(x-x1) + abs(y-y1)

                if dist < best:
                    besti = index
                    best = dist
        return besti