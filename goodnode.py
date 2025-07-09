class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            max_val = max(max_val, node.val)
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)
            return left + right + (1 if node.val >= max_val else 0)
        
        return dfs(root, float('-inf'))
