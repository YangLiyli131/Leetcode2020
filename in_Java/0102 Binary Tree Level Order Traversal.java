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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        if(root == null) return res;
        q.add(root);
        List<Integer> cur;
        TreeNode x;
        int n;
        while(q.size() != 0){
            cur = new ArrayList<>();
            n = q.size();
            for(int i = 0; i < n; i++){
                x = q.poll();
                if(x.left != null) q.add(x.left);
                if(x.right != null) q.add(x.right);
                cur.add(x.val);
            }
            res.add(cur);
        }
        return res;
    }
}