class Solution {
    public String minRemoveToMakeValid(String s) {
        if(s == null || s.length() == 0) return s;
        Stack<Integer> st = new Stack<>(); // store the index to be ignored in the result
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(') st.push(i);
            if(s.charAt(i) == ')'){
                if(st.isEmpty()) st.push(i);
                else{
                    if(s.charAt(st.peek()) == '(') st.pop();
                    else st.push(i);
                }
            }
        }
        Set<Integer> hs = new HashSet<>();
        while(!st.isEmpty()) hs.add(st.pop());
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            if(hs.contains(i)) continue;
            sb.append(s.substring(i,i+1));
        }
        return sb.toString();
    }
}