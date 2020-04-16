/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return head;
        ListNode d = new ListNode(0);
        d.next = head;
        ListNode pre = d;
        ListNode cur = head;
        ListNode next = cur.next;
        while(next != null){
            if(cur.val == next.val){
                while(next != null && cur.val == next.val){
                    next = next.next;
                }
                pre.next = next;
                cur = next;
                if(cur != null) next = cur.next;
            }else{
                pre = cur;
                cur = next;
                next = cur.next;
            }
        }
        return d.next;
    }
}