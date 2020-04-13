class Solution {
    public int strStr(String haystack, String needle) {
        if(needle == null || needle.length() == 0) return 0;
        if(haystack == null || haystack.length() == 0) return -1;
        int n = needle.length();
        for(int i = 0; i <= haystack.length() - n; i++){
            if(haystack.substring(i,i+n).equals(needle)) return i;
        }
        return -1;
    }
}