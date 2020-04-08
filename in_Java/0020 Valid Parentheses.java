class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        
        for(char c : s.toCharArray()){
            if(c == '(' || c == '[' || c == '{') st.push(c);
            else{
                if(!st.isEmpty()){
                    char t = st.peek();
                    if(c == ')' && t == '(') st.pop();
                    else if(c == ']' && t == '[') st.pop();
                    else if(c == '}' && t == '{') st.pop();
                    else return false;
                }else{
                    return false;
                }            
            }
        }
        return st.isEmpty();
    }
}