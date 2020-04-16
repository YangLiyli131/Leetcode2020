class Solution {
    public int smallestRangeI(int[] A, int K) {
        int mmin = A[0];
        int mmax = A[0];
        for(int i : A){
            mmin = Math.min(mmin,i);
            mmax = Math.max(mmax,i);
        }
        if(mmax - mmin > K+K) return mmax - mmin - K - K;
        else return 0;
    }
}