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
    public int deepestLeavesSum(TreeNode root) {
        if(root == null) return 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        TreeNode cur;
        int n;
        List<Integer> L = new ArrayList<>();
        while(q.size() != 0){
            n = q.size();
            L = new ArrayList<>();
            while(n-- != 0){
                cur = q.poll();
                L.add(cur.val);
                if(cur.left != null) q.add(cur.left);
                if(cur.right != null) q.add(cur.right);
            }
        }
        int res = 0;
        for(int i : L) res += i;
        return res;
    }
}