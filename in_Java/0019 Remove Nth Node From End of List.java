/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int leng = 0;
        ListNode d = head;
        while(d != null){
            d = d.next;
            leng++;
        }
        if(n == leng) return head.next;
        ListNode nh = head;
        int dis = leng - 1 - n;
        while(dis != 0){
            nh = nh.next;
            dis--;
        }
        nh.next = nh.next.next;
        return head;
    }
}