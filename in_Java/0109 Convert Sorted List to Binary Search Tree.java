/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null) return null;
        if(head.next == null) return new TreeNode(head.val);
        ListNode slow = head, pre = null, fast = head;
        while(fast != null && fast.next != null){
            pre = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        //System.out.println(slow.val);
        TreeNode root = new TreeNode(slow.val);
        ListNode right = slow.next;
        ListNode left = head;
        //System.out.println(left.val);
        //System.out.println(right.val);
        pre.next = null;
        root.left = sortedListToBST(left);
        root.right = sortedListToBST(right);
        return root;
    }
}