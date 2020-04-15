class Solution {
    public boolean rotateString(String A, String B) {
        if(A == null && B == null) return true;
        if(A.length() == 0 && B.length() == 0) return true;
        if(A == null || B == null) return false;
        if(A.length() > B.length()) return false;
        String A2 = A + A;
        for(int i = 0; i < A2.length() - B.length(); i++){
            if(A2.substring(i, i + B.length()).equals(B)) return true;
        }
        return false;
    }
}