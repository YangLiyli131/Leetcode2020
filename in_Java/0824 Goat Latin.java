class Solution {
    public String toGoatLatin(String S) {
        String res = "";
        String[] st = S.split(" ");
        int n;
        for(int i = 0; i < st.length; i++){
            if(startV(st[i])){
                st[i] += "ma";
            }else{
                st[i] = st[i].substring(1,st[i].length()) + st[i].substring(0,1) + "ma";
            }
            n = i + 1;
            while(n != 0){
                st[i] += "a";
                n--;
            }
        }
        for(int i = 0; i < st.length-1; i++){
            res += st[i] + " ";
        }
        return res + st[st.length-1];
    }
    private boolean startV(String x){
        char c = x.charAt(0);
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') return true;
        else if(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') return true;
        else return false;
    }
}