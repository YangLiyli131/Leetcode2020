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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root == null) return res;
        helper(res,root);
        return res;
    }
    private void helper(List<Integer> res, TreeNode root){
        if(root == null) return;
        helper(res,root.left);
        helper(res,root.right);
        res.add(root.val);
    }
}

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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root == null) return res;
        Stack<TreeNode> st1 = new Stack<>();
        Stack<TreeNode> st2 = new Stack<>();
        st1.push(root);
        while(!st1.isEmpty()){
            TreeNode cur = st1.pop();
            st2.push(cur);
            if(cur.left != null) st1.push(cur.left);
            if(cur.right != null) st1.push(cur.right);
        }
        while(!st2.isEmpty()) res.add(st2.pop().val);
        return res;
    }
}