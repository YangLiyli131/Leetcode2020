class Solution {
    public boolean isValid(String S) {
        Stack<Character> st = new Stack<>();
        for(int i = 0; i < S.length(); i++){
            if(st.size() < 2){
                st.push(S.charAt(i));
                continue;
            }
            char pre = st.pop();
            char two = st.pop();
            if(S.charAt(i) == 'c' && pre == 'b' && two == 'a') continue;
            else{
                st.push(two);st.push(pre);st.push(S.charAt(i));
            }
        }
        return st.isEmpty();
    }
}