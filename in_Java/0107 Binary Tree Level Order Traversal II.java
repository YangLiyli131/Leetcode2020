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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        if(root == null) return res;
        q.add(root);
        TreeNode cur;
        int len;
        List<Integer> temp;
        while(q.size() != 0){
            len = q.size();
            temp = new ArrayList<Integer>();
            while(len != 0){
                cur = q.poll();
                temp.add(cur.val);
                if(cur.left != null) q.add(cur.left);
                if(cur.right != null) q.add(cur.right);
                len--;
            }
            res.add(0,temp);
        }
        return res;
    }
}