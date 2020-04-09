class Solution {
    public String toLowerCase(String str) {
        char[] ch = str.toCharArray();
        for(int i = 0; i < ch.length; i++){
            char c = ch[i];
            if(c >= 'A' && c <= 'Z'){
                ch[i] = Character.toLowerCase(c);
            }
        }
        return String.valueOf(ch);
    }
}