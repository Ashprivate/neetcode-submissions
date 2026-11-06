class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k
        windowSum = sum(arr[:k])
        
        count = 1 if windowSum >= target else 0

        for R in range(k, len(arr)):

            windowSum+=arr[R]
            windowSum-=arr[R-k]

            if windowSum >= target:
                count+=1

            

        return count        


