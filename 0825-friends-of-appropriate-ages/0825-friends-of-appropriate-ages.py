class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Time: O(n^2)
        # Space:
        def friendRequests(a,b):
            if b <= 0.5 * a + 7:
                return False
            if b > a:
                return False 
            return True 



        age_groups = collections.Counter(ages)
        total_requests = 0 

        for a, num_a in age_groups.items():
            for b, num_b in age_groups.items():
                if friendRequests(a,b):
                    total_requests += num_a * num_b 
                    # to handle self requests 
                    if a == b:
                        total_requests -= num_a
        
        return total_requests