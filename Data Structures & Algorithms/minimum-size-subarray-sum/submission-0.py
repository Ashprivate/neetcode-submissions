class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        minlength = float('inf')
        windowSum = 0

        for R in range(len(nums)):
            
            windowSum+=nums[R]

            while windowSum >= target:
                minlength = min(minlength, R-L+1)

                windowSum-=nums[L]
                L+=1

        return 0 if minlength == float('inf') else minlength

