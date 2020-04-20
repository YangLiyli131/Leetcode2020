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
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums == null || nums.length == 0) return null;
        int i = 0, j = nums.length-1;
        int m = i + (j-i)/2;
        TreeNode root = new TreeNode(nums[m]);   
        int[] left = new int[m];
        int[] right = new int[j-m];
        for(int id = 0; id <= m-1; id++) left[id] = nums[id];
        for(int idd = 0; idd < j-m; idd++) right[idd] = nums[idd + m + 1];        
        root.left = sortedArrayToBST(left);
        root.right = sortedArrayToBST(right);
        return root;
    }
}