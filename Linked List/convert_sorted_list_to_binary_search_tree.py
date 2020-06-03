def helper(treelist):
	if len(treelist) == 0:
		return None
	if len(treelist) == 1:
		return treelist[0]
	mid = len(treelist) // 2
	treelist[mid].left = helper(treelist[:mid])
	treelist[mid].right = helper(treelist[mid+1:])
	return treelist[mid]

class Solution:
	def sortedListToBST(self, head: ListNode) -> TreeNode:
		if not head: 
			return None
		treelist = []
		while head:
			treelist.append(TreeNode(head.val))
			head = head.next
		return helper(treelist)