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
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> L = new ArrayList<>();
        Stack<TreeNode> st = new Stack<>();
        TreeNode cur = root;
        while(cur != null || !st.isEmpty()){
            while(cur != null){
                st.push(cur);
                cur = cur.left;
            }
            cur = st.pop();
            L.add(cur.val);
            cur = cur.right;
        }
        return L.get(k-1);
    }
}