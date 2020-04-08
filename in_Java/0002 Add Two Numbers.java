/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0);
        ListNode dummy = res;
        int overflow = 0;
        while(l1 != null && l2 != null){
            int cur = l1.val + l2.val + overflow;
            if(cur > 9){
                overflow = 1;
                cur %= 10;
            }else{
                overflow = 0;
            }
            dummy.next = new ListNode(cur);
            dummy = dummy.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        while(l1 != null){
            int t = l1.val + overflow;
            if(t > 9){
                overflow = 1;
                t %= 10;
            }else{
                overflow = 0;
            }
            dummy.next = new ListNode(t);
            dummy = dummy.next;
            l1 = l1.next;
        }
        while(l2 != null){
            int w = l2.val + overflow;
            if(w > 9){
                overflow = 1;
                w %= 10;
            }else{
                overflow = 0;
            }
            dummy.next = new ListNode(w);
            dummy = dummy.next;
            l2 = l2.next;
        }
        if(overflow == 1){
            dummy.next = new ListNode(1);
        }
        return res.next;
    }
}