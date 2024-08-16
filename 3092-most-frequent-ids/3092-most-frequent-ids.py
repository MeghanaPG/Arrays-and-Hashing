from sortedcontainers import SortedList

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        sl = SortedList()
        f = collections.Counter()

        ans = []
        for x, k in zip(nums, freq):
            if x not in f:
                f[x] = 0 
                sl.add((0,x))

            sl.remove((f[x], x))
            f[x] += k 
            sl.add((f[x], x))

            if len(sl) == 0:
                ans.append(0)
            else:
                ans.append(sl[-1][0])
        return ans

