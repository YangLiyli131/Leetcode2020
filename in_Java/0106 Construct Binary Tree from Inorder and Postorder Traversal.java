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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        for(int i = 0; i < inorder.length; i++) hm.put(inorder[i],i);
        TreeNode r = helper(inorder, 0, inorder.length-1, postorder, 0, postorder.length-1, hm);
        return r;
    }
    private TreeNode helper(int[] in, int inStart, int inEnd, int[] post, int postStart, int postEnd, HashMap<Integer,Integer> hm){
        if(inStart > inEnd || postStart > postEnd) return null;
        TreeNode root = new TreeNode(post[postEnd]);
        int id = hm.get(root.val);
        int dis = inEnd - id;
        root.right = helper(in, id+1, inEnd, post, postEnd-dis, postEnd-1, hm);
        root.left = helper(in, inStart, id-1, post, postStart, postEnd-dis-1, hm);
        return root;
    }
}