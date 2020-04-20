class Solution {
    public String reverseStr(String s, int k) {
        int len = k+k;
        StringBuilder sb = new StringBuilder();
        int num = s.length() / (k+k);
        int rest = s.length() % (k+k);
        
        for(int i = 0; i < num; i++){
            String cur = s.substring(0 + len * i, len + len * i);
            String a = cur.substring(0, k);
            String b = cur.substring(k, cur.length());
            sb.append(rev(a));
            sb.append(b);
        }
        if(rest != 0){
            String last = s.substring(s.length() - rest, s.length());
            if(last.length() <= k) sb.append(rev(last));
            else{
                sb.append(rev(last.substring(0,k)));
                sb.append(last.substring(k,last.length()));
            }
        }
        return sb.toString();
    }
    private String rev(String s){
        char[] ch = s.toCharArray();
        int i = 0;
        int j = ch.length-1;
        while(i < j){
            char t = ch[i];
            ch[i] = ch[j];
            ch[j] = t;
            i++;
            j--;
        }
        return String.valueOf(ch);
    }
}