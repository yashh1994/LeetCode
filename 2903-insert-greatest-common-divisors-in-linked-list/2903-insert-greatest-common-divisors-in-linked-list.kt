/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun insertGreatestCommonDivisors(head: ListNode?): ListNode? {
        var head = head
        if(head == null || head.next == null){
            return head
        }
        var ans = ListNode(0)
        var temp = ans
        while(head?.next != null){
            temp.next = ListNode(head.`val`)
            var t = find(temp.next.`val`,head.next.`val`)
            temp.next.next = ListNode(t)
            temp = temp.next.next
            head = head.next
        }
        temp.next = head
        return ans.next
    }
    fun find(n1: Int,n2: Int): Int{
        var max = maxOf(n1,n2)
        var min = minOf(n1,n2)
        var ans = 0
        for(i in 1..min){
            if(max%i == 0 && min%i == 0){
                ans = i
            }
        }
        return ans
    }
}