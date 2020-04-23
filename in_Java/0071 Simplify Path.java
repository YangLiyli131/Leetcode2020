class Solution {
    public String simplifyPath(String path) {
        Stack<String> st = new Stack<>();
        int start;
        int end;
        for(int i = 0; i < path.length(); ){
            while(i < path.length() && path.charAt(i) == '/') i++;
            start = i;
            while(i < path.length() && path.charAt(i) != '/') i++;
            end = i;
            i++;
            String cur = path.substring(start,end);//System.out.println(cur);
            if(cur.equals(".") || cur.equals("")) continue;
            else if(cur.equals("..")){
                if(!st.isEmpty()) st.pop();
            }else st.push(cur);
        }
        StringBuilder sb = new StringBuilder();
        if(st.isEmpty()) return "/";
        while(!st.isEmpty()){
            sb.insert(0,st.pop());
            sb.insert(0,"/");
        }
        return sb.toString();
    }
}