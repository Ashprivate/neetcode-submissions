class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for num in nums:
            counts[num] += 1
        
        print("count", counts)
        i=0
        for index,c in enumerate(counts):
            for j in range(c):
                nums[i] = index
                i+=1

        return nums        
            
        