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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if(root == null) return res;
        //res.add(root.val);
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int len;
        int curmax; 
        TreeNode cur;
        while(q.size() != 0){
            curmax = Integer.MIN_VALUE;
            len = q.size();
            while(len-- != 0){
                cur = q.poll();
                curmax = Math.max(curmax,cur.val);
                if(cur.left != null) q.add(cur.left);
                if(cur.right != null) q.add(cur.right);
            }
            res.add(curmax);
        }
        return res;
    }
}