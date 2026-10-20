class Solution:
    def countBits(self, n: int) -> List[int]:
        
        
        bits=[]

        for i in range(0,n+1):
          count = 0
          while i > 0:
            if i & 1:
                  count +=1
            i = i >> 1
          bits.append(count)

        return bits  