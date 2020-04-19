class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<String> st = new Stack<>();
        for(char c : s.toCharArray()){
            if(!st.isEmpty() && c == st.peek().charAt(0)){
                String cur = st.peek();
                int curlen = Integer.parseInt(cur.substring(1,cur.length()));
                if(curlen == k-1){
                    while(curlen-- != 0) st.pop();
                }else{
                    st.push(Character.toString(c) + (curlen+1));
                }                
            }else{
                st.push(Character.toString(c) + "1");
            }
        }
        StringBuilder sb = new StringBuilder();
        while(!st.isEmpty()){
            //System.out.println(st.peek());
            sb.insert(0, st.pop().charAt(0));
        }
        return sb.toString();
    }
}