/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        int l = 0;
        ListNode d = head;
        while(d != null){
            l++;
            d = d.next;
        }
        if(l <= 1) return true;
        int dis = 0;
        if(l % 2 == 0) dis = l/2;
        else dis = l/2+1;
        ListNode newH = head;
        while(dis != 0){
            newH = newH.next;
            dis--;
        }
        ListNode b = rev(newH);
        ListNode a = head;
        while(b != null){
            if(a.val != b.val) return false;
            a = a.next;
            b = b.next;
        }
        return true;
    }
    private ListNode rev(ListNode n){
        ListNode pre = null;
        ListNode cur = n;
        ListNode next = null;
        while(cur != null){
            next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
}