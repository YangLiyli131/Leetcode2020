class Solution {
    public boolean isPalindrome(String s) {
        if(s == null || s.length() <= 1) return true;
        int i = 0;
        int j = s.length()-1;
        while(i < j){
            while(!isV(s.charAt(i)) && i < j) i++;
            while(!isV(s.charAt(j)) && i < j) j--;
            if(Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) return false;
            i++;
            j--;
        }
        return true;
    }
    private boolean isV(char c){
        if(c >= 'a' && c <= 'z') return true;
        if(c >= 'A' && c <= 'Z') return true;
        if(c >= '0' && c <= '9') return true;
        return false;
    }
}