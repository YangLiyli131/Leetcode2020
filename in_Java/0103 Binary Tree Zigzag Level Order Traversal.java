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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        if(root == null) return res;
        q.add(root);
        TreeNode cur;
        int len;
        int id = 0;
        List<Integer> temp;
        while(q.size() != 0){
            len = q.size();
            temp = new ArrayList<>();
            while(len != 0){
                cur = q.poll();
                if(id % 2 == 0){
                    temp.add(cur.val);
                }else{
                    temp.add(0,cur.val);
                }
                if(cur.left != null) q.add(cur.left);
                if(cur.right != null) q.add(cur.right);
                len--;
            }
            id++;
            res.add(temp);
        }
        return res;
    }
}