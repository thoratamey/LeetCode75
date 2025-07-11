    def maxLevelSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, list: List, level: int) -> None:
            if not node:
                return
            if len(list) == level:
                list.append(node.val)
            else:
                list[level] += node.val
            dfs(node.left, list, level + 1)
            dfs(node.right, list, level + 1)
        list = []    
        dfs(root, list, 0)
        return 1 + list.index(max(list))
