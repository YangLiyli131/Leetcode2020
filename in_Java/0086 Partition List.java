/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode a = new ListNode(0);
        ListNode b = new ListNode(0);
        ListNode h = head;
        ListNode newa = a;
        ListNode newb = b;
        ListNode next;
        while(h != null){
            next = h.next;
            if(h.val < x){
                a.next = h;
                a = a.next;
                a.next = null;
            }else{
                b.next = h;
                b = b.next;
                b.next = null;
            }
            h = next;
        }
        a.next = newb.next;
        return newa.next;
    }
}