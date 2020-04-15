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
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        Stack<TreeNode> st = new Stack<>();
        TreeNode cur = cloned;
        while(cur != null || !st.isEmpty()){
            while(cur != null){
                if(cur.val == target.val) return cur;
                st.push(cur);
                cur = cur.left;
            }
            cur = st.pop();
            cur = cur.right;
        }
        return cur;
    }
}