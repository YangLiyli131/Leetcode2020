class Solution {
    public boolean validPalindrome(String s) {
        if(s == null || s.length() == 0) return true;
        int i = 0, j = s.length()-1;
        while(i < j){
            if(s.charAt(i) != s.charAt(j)){
                String x = s.substring(0,i) + s.substring(i+1,s.length());
                String y = s.substring(0,j) + s.substring(j+1,s.length());
                return isP(x) || isP(y);
            }else{
                i++;
                j--;
            }
        }
        return true;
    }
    private boolean isP(String x){
        int i = 0, j = x.length()-1;
        while(i < j){
            if(x.charAt(i) != x.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
}