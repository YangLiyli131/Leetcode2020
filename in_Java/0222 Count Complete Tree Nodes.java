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
    public int countNodes(TreeNode root) {
        if(root == null) return 0;
        int res = 1;
        int rightn = height(root.right);
        int h = height(root);
        int leftn = h-1;
        
        if(leftn == rightn){
            res += Math.pow(2,leftn)-1;
            res += bfs(root.right);
        }else{
            res += Math.pow(2,rightn)-1;
            res += bfs(root.left);
        }
        return res;
    }
    private int height(TreeNode t){
        int res = 0;
        while(t != null){
            res++;
            t = t.left;
        }
        return res;
    }
    private int bfs(TreeNode r){
        if(r == null) return 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(r);
        TreeNode cur;
        int n;
        int res = 0;
        while(!q.isEmpty()){
            n = q.size();
            while(n-- != 0){
                cur = q.poll();
                res++;
                if(cur.left != null) q.add(cur.left);
                if(cur.right != null) q.add(cur.right);
            }
        }
        return res;
    }
}