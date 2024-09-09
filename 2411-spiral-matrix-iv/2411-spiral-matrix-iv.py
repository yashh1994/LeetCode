# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        step = 0
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        while step <= min(m, n) // 2:
            for i in range(step, n - step):
                if head:
                    ans[step][i] = head.val
                    head = head.next
                else:
                    return ans

            for i in range(step + 1, m - step):
                if head:
                    ans[i][n - step - 1] = head.val
                    head = head.next
                else:
                    return ans

            if m - step - 1 > step:  
                for i in range(n - step - 2, step - 1, -1):
                    if head:
                        ans[m - step - 1][i] = head.val
                        head = head.next
                    else:
                        return ans

            if n - step - 1 > step:  
                for i in range(m - step - 2, step, -1):
                    if head:
                        ans[i][step] = head.val
                        head = head.next
                    else:
                        return ans

            step += 1

        return ans
