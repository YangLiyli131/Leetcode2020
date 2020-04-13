class Solution {
    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();
        String[] ss = s.split(" ");
        for(String x : ss){
            sb.append(rev(x));
            sb.append(" ");
        }
        return sb.toString().strip();
    }
    private String rev(String s){
        char[] ch = s.toCharArray();
        int i = 0;
        int j = ch.length-1;
        char t;
        while(i < j){
            t = ch[i];
            ch[i] = ch[j];
            ch[j] = t;
            i++;
            j--;
        }
        return String.valueOf(ch);
    }
}