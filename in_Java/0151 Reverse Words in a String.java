class Solution {
    public String reverseWords(String s) {
        String[] st = s.split(" ");
        String res = "";
        for(int i = st.length-1; i >= 0; i--){
            if(st[i].length() == 0) continue;
            res += st[i] + " ";
        }
        return res.strip();
    }
}