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
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        TreeNode cur;
        int level = 1;
        int n;
        while(q.size() != 0){
            n = q.size();
            while(n-- != 0){
                cur = q.poll();
                if(cur.left == null && cur.right == null) return level;
                if(cur.left != null) q.add(cur.left);
                if(cur.right != null) q.add(cur.right);
            }
            level++;
        }
        return level;
    }
}