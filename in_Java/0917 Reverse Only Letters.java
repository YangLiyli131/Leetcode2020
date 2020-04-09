class Solution {
    public String reverseOnlyLetters(String S) {
        char[] ch = S.toCharArray();
        int i = 0;
        int j = ch.length-1;
        char t;
        while(i < j){
            while(!isL(ch[i]) && i < j) i++;
            while(!isL(ch[j]) && i < j) j--;
            t = ch[i];
            ch[i] = ch[j];
            ch[j] = t;
            i++;
            j--;
        }
        return String.valueOf(ch);
    }
    private boolean isL(char c){
        if(c >= 'a' && c <= 'z') return true;
        else if(c >= 'A' && c <= 'Z') return true;
        else return false;
    }
}