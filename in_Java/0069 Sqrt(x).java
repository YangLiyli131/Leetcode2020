class Solution {
    public int mySqrt(int x) {
        if(x == 0) return 0;
        int i = 1;
        int j = x;
        int m;
        while(i <= j){
            m = i + (j - i) / 2;
            if(x / m >= m && (m+1) > x / (m+1)) return m;
            else if(m < x / m) i = m+1;
            else j = m-1;
        }
        return -1;
    }
}