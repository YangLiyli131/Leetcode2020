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
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        if(root == null) return res;
        q.add(root);
        TreeNode cur;
        int len;
        int lenn;
        long s;
        while(q.size() != 0){
            len = q.size();
            lenn = len;
            s = 0;
            while(len != 0){
                cur = q.poll();
                s += (long)cur.val;
                if(cur.left != null) q.add(cur.left);
                if(cur.right != null) q.add(cur.right);
                len--;
            }
            res.add(s / (double)lenn);
        }
        return res;
    }
}