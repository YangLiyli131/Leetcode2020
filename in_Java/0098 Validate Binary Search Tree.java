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
    public boolean isValidBST(TreeNode root) {
        // inorder
        List<Integer> L = new ArrayList<>();
        if(root == null) return true;
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
        // check if it is acsending
        for(int i = 1; i < L.size(); i++){
            if(L.get(i) <= L.get(i-1)) return false;
        }
        return true;
    }
}