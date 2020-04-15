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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if(root == null) return res;
        Stack<TreeNode> stn = new Stack<>();
        Stack<String> sts = new Stack<>();
        stn.push(root);
        sts.push("");
        while(!stn.isEmpty()){
            TreeNode cur = stn.pop();
            String now = sts.pop();
            if(cur.left == null && cur.right == null) res.add(now + cur.val);
            if(cur.left != null){
                stn.push(cur.left);
                sts.push(now + cur.val + "->");
            }
            if(cur.right != null){
                stn.push(cur.right);
                sts.push(now + cur.val + "->");
            }
        }
        return res;
    }
}