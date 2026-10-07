class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        mid = ( low + high ) // 2

        while low <= high:
            pilehrs = 0
            for p in piles:
                pilehrs = pilehrs + math.ceil(p/mid)

            if pilehrs > h:
                low = mid + 1;
            else:
                high = mid -1;
            
            mid = (low + high) // 2

        return low    



