class Solution {
    public char findTheDifference(String s, String t) {
        int[] d = new int[26];
        int tt = 0;
        for(char c : s.toCharArray()){
            d[c - 'a']++;
        }
        for(char c : t.toCharArray()){
            d[c - 'a']--;
        }
        for(int i = 0; i < 26; i++){
            if(d[i] != 0){
                tt = i;
                break;
            }
        }
        return (char)((int)'a' + tt);
    }
}