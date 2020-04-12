class Solution {
    public boolean detectCapitalUse(String word) {
        char[] ch = word.toCharArray();
        boolean f = isC(ch[0]);
        int n = 0;
        for(char c : ch){
            if(isC(c)) n++;
        }
        if(n == 0 || n == word.length()) return true;
        else if(n == 1 && f) return true;
        else return false;
    }
    private boolean isC(char c){
        return c >= 'A' && c <= 'Z';
    }
}