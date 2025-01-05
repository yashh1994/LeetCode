# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:


    def serialize(self, root):
        if not root: return ''
        res = []
        q = deque([root])

        while q:
            cur = q.popleft()
            if cur:
                q.append(cur.left)
                q.append(cur.right)
                res.append(str(cur.val))
            else:
                res.append("None")

        while res and res[-1] == "None":
            res.pop()

        ser = ','.join(res)
        return ser 



        
    def deserialize(self, data):
        if not data: return []
        return [int(n) if n != 'None' else None for n in data.split(',')]
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))