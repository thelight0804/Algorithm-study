"""
Date:
  23.06.12
Number:
  LeetCode 257
Title:
   Binary Tree Paths
Level:
  Easy
Author:
  thelight0804
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if not root: return []

    output = []

    def dfs(crntNode, leaf):
      #exit recursive method
      if not crntNode.left and not crntNode.right:
        output.append(leaf+str(crntNode.val))
        return

      #call recursive method
      if crntNode.left:
        dfs(crntNode.left, leaf+str(crntNode.val)+"->")
        
      if crntNode.right:
        dfs(crntNode.right, leaf+str(crntNode.val)+"->")
    
    #start Backtracking
    dfs(root, "")

    return output