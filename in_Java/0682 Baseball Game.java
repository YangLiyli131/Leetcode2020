class Solution {
    public int calPoints(String[] ops) {
        Stack<Integer> st = new Stack<>();
        int last = 0;
        int last2 = 0;
        for(String s : ops){
            if(s.equals("+")){
                last = st.pop();
                last2 = st.peek();
                st.push(last);
                st.push(last + last2);
            }else if(s.equals("D")){
                st.push(2 * st.peek());
            }else if(s.equals("C")){
                st.pop();
            }else{
                st.push(Integer.parseInt(s));
            }
        }
        int res = 0;
        for(int i : st) res += i;
        return res;
    }
}