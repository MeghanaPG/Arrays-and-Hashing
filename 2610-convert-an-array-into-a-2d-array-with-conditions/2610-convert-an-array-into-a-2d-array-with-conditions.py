class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # Time, Space: O(n)
        count = defaultdict(int)
        res = []

        # we only insert a row if it doesn't exist
        for n in nums:
            row = count[n]
            if len(res) == row:
                res.append([])
            
            res[row].append(n)
            count[n] += 1
        return res 