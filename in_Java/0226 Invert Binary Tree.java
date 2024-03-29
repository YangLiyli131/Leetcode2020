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
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return root;
        if(root.left == null && root.right == null) return root;
        TreeNode temp = root.right;
        root.right = root.left;
        root.left = temp;
        
        //TreeNode t = invertTree(root.left);
        root.left = invertTree(root.left);
        root.right = invertTree(root.right);
        
        return root;
    }
}