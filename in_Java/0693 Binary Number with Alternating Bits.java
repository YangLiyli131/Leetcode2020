class Solution {
    public boolean hasAlternatingBits(int n) {
        int cur = n & 1;
        n >>=1;
        while(n != 0){
            int newcur = n & 1;
            if(newcur == cur) return false;
            cur = newcur;
            n /= 2;
        }
        return true;
    }
}