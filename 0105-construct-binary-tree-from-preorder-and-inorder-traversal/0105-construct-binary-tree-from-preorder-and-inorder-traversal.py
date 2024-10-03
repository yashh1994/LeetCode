class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def go(pre, cur, ino):
            if cur == len(pre) or not ino:
                return None
            temp = TreeNode(pre[cur])
            index = ino.index(pre[cur])
            left_ino = ino[:index]
            right_ino = ino[index+1:]
            temp.left = go(pre, cur + 1, left_ino)
            temp.right = go(pre, cur + len(left_ino) + 1, right_ino)
            return temp
            
        ans = go(preorder, 0, inorder)
        return ans
