# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queve = deque()

        if root:
            queve.append(root)

        level = 0
        result=[]

        while len(queve) > 0:
            level_size = len(queve)
            for i in range(len(queve)):

                curr = queve.popleft()
                if i == level_size-1:
                    result.append(curr.val) 
                
                if curr.left:
                    queve.append(curr.left)
                if curr.right:
                    queve.append(curr.right)
         
        return result