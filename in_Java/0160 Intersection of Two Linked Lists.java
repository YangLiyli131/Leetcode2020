/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA, b = headB;
        int lena = 0, lenb = 0;
        while(a != null){
            lena++;
            a = a.next;
        }
        while(b != null){
            lenb++;
            b = b.next;
        }
        int d;
        if(lena > lenb){
            d = lena-lenb;
            while(d-- != 0){
                headA = headA.next;
            }
        }
        if(lena < lenb){
            d = lenb-lena;
            while(d-- != 0){
                headB = headB.next;
            }
        }
        while(headA != null && headB != null){
            if(headA == headB) return headA;
            headA = headA.next;
            headB = headB.next;
        }
        return null;
    }
}