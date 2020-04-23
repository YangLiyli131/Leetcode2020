class Solution {
    public boolean find132pattern(int[] nums) {
        Stack<Integer> st = new Stack<>();
        int curmin = Integer.MAX_VALUE;
        for(int i : nums){
            if(i <= curmin){
                curmin = i;
            }else{
                while(!st.isEmpty()){
                    if(st.peek() >= i) break;
                    st.pop(); // pop away smaller value
                    if(st.pop() > i) return true; // after popping smaller value, check for Ak
                }
                st.push(i);
                st.push(curmin);
            }
        }
        return false;
    }
}