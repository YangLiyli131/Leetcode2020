/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        int l = 0;
        ListNode d = head;
        while(d != null){
            d = d.next;
            l++;
        }
        int res = 0;
        while(head != null){
            res += head.val * (Math.pow(2,l-1));
            head = head.next;
            l--;
        }
        return res;
    }
}