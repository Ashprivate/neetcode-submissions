class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if row[0] <= target <= row[-1]:
                left, right = 0, len(row) -1

                mid = ( left + right ) // 2;

                while left <= right:

                    if target < row[mid]:
                        right = mid - 1
                    elif target > row[mid]:
                        left = mid +1
                    else:
                        return True

                    mid = ( left + right ) // 2;

        return False

        
       
            
