/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        int leng = 0;
        ListNode d = head;
        while(d != null){
            d = d.next;
            leng++;
        }
        if(head == null || leng == 0 || k == 0) return head;
        int kk = k % leng;
        if(kk == 0) return head;
        
        int dis = leng - kk;
        ListNode newh = head;
        ListNode tail = null;
        while(dis != 0){
            newh = newh.next;
            dis--;
            if(dis == 1) tail = newh;
        }
        if(tail != null) tail.next = null;
        ListNode dd = newh;
        while(dd.next != null){
            dd = dd.next;
        }
        if(leng - kk == 1) head.next = null;
        dd.next = head;
        return newh;
    }
}