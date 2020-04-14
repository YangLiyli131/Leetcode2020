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
    public boolean isCousins(TreeNode root, int x, int y) {
        Queue<TreeNode> q = new LinkedList<>();
        int level_x = 0;
        int level_y = 0;
        int parent_x = 0;
        int parent_y = 0;
        q.add(root);
        int len;
        TreeNode cur;
        int id = 0;
        while(q.size() != 0){
            len = q.size();
            while(len-- != 0){
                cur = q.poll();
                if(cur.left != null){
                    if(cur.left.val == x){
                        level_x = id+1;
                        parent_x = cur.val;
                    }
                    if(cur.left.val == y){
                        level_y = id+1;
                        parent_y = cur.val;
                    }
                    q.add(cur.left);
                }
                if(cur.right != null){
                    if(cur.right.val == x){
                        level_x = id+1;
                        parent_x = cur.val;
                    }
                    if(cur.right.val == y){
                        level_y = id+1;
                        parent_y = cur.val;
                    }
                    q.add(cur.right);
                } 
            }
            id++;
        }
        return level_x == level_y && parent_x != parent_y;
    }
}