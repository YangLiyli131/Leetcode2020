class Solution {
    public int calculate(String s) {
        if(s == null || s.length() == 0) return 0;
        Stack<Integer> st = new Stack<>();
        int n = 0;
        char sign = '+';
        for(int i = 0; i < s.length(); i++){
            if(Character.isDigit(s.charAt(i))){
                n = n * 10 + s.charAt(i)-'0';
            }
            if(!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ' || i == s.length()-1){
                if(sign == '+') st.push(n);
                else if(sign == '-') st.push(-n);
                else if(sign == '*') st.push(st.pop() * n);
                else st.push(st.pop()/n);
                sign = s.charAt(i);
                n = 0;
            }
        }
        int res = 0;
        while(!st.isEmpty()) res += st.pop();
        return res;
    }
}