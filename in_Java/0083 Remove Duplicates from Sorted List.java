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
        ListNode d = head;
        while(d != null && d.next != null){
            if(d.val == d.next.val){
                d.next = d.next.next;
            }
            else d = d.next;
        }
        return head;
    }
}