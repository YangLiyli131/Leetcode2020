class Solution {
    public int scoreOfParentheses(String S) {
        Stack<String> st = new Stack<>();
        for(char c : S.toCharArray()){
            if(c == '(') st.push(Character.toString(c));
            else{
                if(st.peek().equals("(")){
                    st.pop();
                    st.push("1");
                    continue;
                }
                int n = 0;
                while(!st.isEmpty() && !st.peek().equals("(")){
                    n += Integer.parseInt(st.pop());
                }
                st.pop();
                st.push(String.valueOf(n+n));
            }
        }
        int res = 0;
        while(!st.isEmpty()) res += Integer.parseInt(st.pop());
        return res;
    }
}