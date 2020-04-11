class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> st = new Stack<>();
        int[] temp = new int[nums2.length];
        for(int i = 0; i < nums2.length; i++){
            while(!st.isEmpty() && nums2[st.peek()] < nums2[i]){
                temp[st.peek()] = nums2[i];
                st.pop(); 
            }
            st.push(i);
        }
        while(!st.isEmpty()){
            temp[st.pop()] = -1;
        }
        int[] res = new int[nums1.length];
        for(int i = 0; i < res.length; i++){
            res[i] = temp[idxof(nums2,nums1[i])];
        }
        return res;
    }
    private int idxof(int[] x, int n){
        for(int i = 0; i < x.length; i++){
            if(x[i] == n) return i;
        }
        return -1;
    }
}