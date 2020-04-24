class Solution {
    public int minAddToMakeValid(String S) {
        if(S == null || S.length() == 0) return 0;
        Stack<Character> st = new Stack<>();
        for(char c : S.toCharArray()){
            if(c == '(') st.push(c);
            else{
                if(!st.isEmpty() && st.peek() == '(') st.pop();
                else st.push(c);
            }
        }
        return st.size();
    }
}