class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] t = new int[nums.length * 2];
        for(int i = 0; i < nums.length; i++){
            t[i] = nums[i];
            t[i+nums.length] = nums[i];
        }
        Stack<Integer> st = new Stack<>();
        for(int i = 0; i < t.length; i++){
            while(!st.isEmpty() && t[i] > t[st.peek()]){
                t[st.peek()] = t[i];
                st.pop();
            }
            st.push(i);
        }
        while(!st.isEmpty()) t[st.pop()] = -1;
        int[] res = new int[nums.length];
        for(int i = 0; i < nums.length; i++) res[i] = t[i];
        return res;
    }
}