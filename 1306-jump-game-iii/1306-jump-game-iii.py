class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # DFS
        # O(n)
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True 
            
            # to avoid re-visiting the same index 
            arr[start] = - arr[start]
            return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False