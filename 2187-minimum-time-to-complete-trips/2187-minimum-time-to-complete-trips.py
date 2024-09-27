class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # Time: O(n.log(m.k))
        l, r = 1, max(time)*totalTrips

        def timeEnough(given_time):
            actual_trips = 0 
            for t in time:
                actual_trips += given_time//t
            return actual_trips >= totalTrips 

        while l < r:
            mid = (l + r)//2
            if timeEnough(mid):
                r = mid 
            else:
                l = mid + 1
        return l 