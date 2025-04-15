# Approach:
# 1. Perform level order traversal (BFS) using a queue to process the tree level by level.
# 2. For each level, collect all node values in a list.
# 3. Append the maximum value from each level to the result list.

# Time Complexity: O(N) — where N is the number of nodes in the tree (each node is visited once)
# Space Complexity: O(N) — for storing the queue and result list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            level = []

            for _ in range(qLen):
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            
            if level:
                res.append(max(level))
        
        return res
