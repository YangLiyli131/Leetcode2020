class Solution {
    public String reverseVowels(String s) {
        char[] ch = s.toCharArray();
        int i = 0; int j = ch.length-1;
        char t;
        while(i < j){
            while(!isV(ch[i]) && i < j) i++;
            while(!isV(ch[j]) && i < j) j--;
            t = ch[i];
            ch[i] = ch[j];
            ch[j] = t;
            i++;
            j--;
        }
        return String.valueOf(ch);
    }
    private boolean isV(char c){
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') return true;
        else if(c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') return true;
        else return false;
    }
}