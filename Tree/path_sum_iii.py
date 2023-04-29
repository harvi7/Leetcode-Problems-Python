# class Solution:
#     totalPaths = 0
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         def dfs(root, start, s):
#             if not root:
#                 return
#             s -= root.val 
#             if s == 0:
#                 self.totalPaths += 1
#             dfs(root.left,False, s)
#             dfs(root.right,False, s)
#             if start: 
#                 dfs(root.left,True,sum)
#                 dfs(root.right,True,sum)
        
#         dfs(root, True, sum)
#         return self.totalPaths

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int: 
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return 

            curr_sum += node.val

            if curr_sum == k:
                count += 1
            count += h[curr_sum - k]

            h[curr_sum] += 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            h[curr_sum] -= 1
            
        count, k = 0, sum
        h = defaultdict(int)
        preorder(root, 0)
        return count