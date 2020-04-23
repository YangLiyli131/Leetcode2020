class Solution {
    public String reverseParentheses(String s) {
        Stack<Character> st = new Stack<>();
        List<Character> temp = new ArrayList<>();
        for(char c : s.toCharArray()){
            if(c != ')') st.push(c);
            else{
                temp = new ArrayList<>();
                while(!st.isEmpty() && st.peek() != '('){
                    temp.add(st.pop());
                }
                st.pop();
                for(char x : temp) st.push(x);
            }
        }
        char[] r = new char[st.size()];
        int id = r.length-1;
        while(!st.isEmpty()) r[id--] = st.pop();
        return String.valueOf(r);
    }
}