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
    public int sumNumbers(TreeNode root) {
        return dfs(root,0);
    }
    private int dfs(TreeNode root, int n){
        if(root == null) return 0;
        if(root.left == null && root.right == null) return n * 10 + root.val;
        return dfs(root.left, n * 10 + root.val) + dfs(root.right,n * 10 + root.val);
    }
}