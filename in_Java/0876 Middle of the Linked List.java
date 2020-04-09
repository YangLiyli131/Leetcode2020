/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        int l = 0;
        ListNode d = head;
        while(d != null){
            l++;
            d = d.next;
        }
        int n = l/2;
        while(n-- != 0) head = head.next;
        return head;
    }
}