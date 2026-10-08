# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queve = deque()

        if root:
            queve.append(root)

        level = 0
        result=[]

        while len(queve) > 0:
            current_level = []
            result.append(current_level)
            for i in range(len(queve)):

                curr = queve.popleft()
                current_level.append(curr.val) 
                
                if curr.left:
                    queve.append(curr.left)
                if curr.right:
                    queve.append(curr.right)
                      
                level+=1

        return result