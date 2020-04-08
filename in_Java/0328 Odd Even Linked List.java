/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode h1 = head;
        if(h1 == null) return head;
        ListNode h2 = h1.next;
        if(h2 == null) return head;
        ListNode d1 = new ListNode(0);
        d1.next = h1;
        ListNode d2 = new ListNode(0);
        d2.next = h2;
        
        while(h1 != null && h1.next != null && h1.next.next != null){
            h1.next = h1.next.next;
            h1 = h1.next;
            if(h1 != null){
                h2.next = h1.next;
                h2 = h2.next;
            }
        }
        h1.next = d2.next;
        return d1.next;
    }
}