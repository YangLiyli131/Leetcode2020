class Solution {
    public String removeOuterParentheses(String S) {
        Stack<String> st = new Stack<>();
        int cum = 0;
        int start = 0;
        for(int i = 0; i < S.length(); i++){
            char c = S.charAt(i);
            if(c == '(') cum++;
            else cum--;
            if(cum == 0){
                st.push(S.substring(start,i+1));
                start = i+1;
            }
        }
        String res = "";
        while(!st.isEmpty()){
            String cur = st.pop();
            res = cur.substring(1,cur.length()-1) + res;
        }
        return res;
    }
}