# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = [0]

        def dfs(root, cur_sum, pre_sum_d):
            if not root: 
                return None
            cur_sum += root.val
            ans[0] += pre_sum_d.get(cur_sum - targetSum, 0)
            pre_sum_d[cur_sum] = pre_sum_d.get(cur_sum, 0) + 1
            
            dfs(root.left, cur_sum, pre_sum_d)
            dfs(root.right, cur_sum, pre_sum_d)

            pre_sum_d[cur_sum] = pre_sum_d.get(cur_sum, 0) - 1
            cur_sum -= root.val

        pre_sum_d = dict()
        pre_sum_d[0] = 1
        cur_sum = 0
        dfs(root, cur_sum, pre_sum_d)

        return ans[0]


        
