class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases: Check structural equivalence
        if not p and not q:
            return True
        if not p or not q:
            return False
            
        # Check value equivalence AND recursively check both subtrees
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))