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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        for(int i = 0; i < inorder.length; i++){
            hm.put(inorder[i],i);
        }
        TreeNode root = helper(preorder, 0, preorder.length-1, inorder, 0, inorder.length-1, hm);
        return root;
    }
    private TreeNode helper(int[] pre, int preStart, int preEnd, int[] in, int inStart, int inEnd, HashMap<Integer,Integer> hm){
        if(preStart > preEnd || inStart > inEnd) return null;
        TreeNode root = new TreeNode(pre[preStart]);
        int id = hm.get(root.val);
        int dis = id - inStart;
        root.left = helper(pre, preStart+1, preStart + dis, in, inStart, id-1, hm);
        root.right = helper(pre, preStart+dis+1, preEnd, in, id+1, inEnd, hm);
        return root;
    }
}