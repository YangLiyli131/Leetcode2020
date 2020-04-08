class Solution {
    public String removeDuplicates(String S) {
        Stack<Character> st = new Stack<>();
        for(char c : S.toCharArray()){
            if(!st.isEmpty() && st.peek() == c){
                st.pop();
            }else{
                st.push(c);
            }
        }
        String res = "";
        while(!st.isEmpty()) res = st.pop().toString() + res;
        return res;
    }
}