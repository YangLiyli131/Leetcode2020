class Solution {
    public int calculate(String s) {
        int res = 0;
        int sign = 1;
        int number = 0;
        Stack<Integer> st = new Stack<>();
        for(char c : s.toCharArray()){
            if(c >= '0' && c <= '9'){
                number = number * 10 + c - '0';
            }else if(c == '+'){
                res += sign * number;
                number = 0;
                sign = 1;
            }else if(c == '-'){
                res += sign * number;
                number = 0;
                sign = -1;
            }else if(c == '('){
                st.push(res);
                st.push(sign);
                res = 0;
                sign = 1;
            }else if(c == ')'){
                res += sign * number;
                number = 0;
                res *= st.pop();
                res += st.pop();
            }
        }
        if(number != 0) res += sign * number;
        return res;
    }
}