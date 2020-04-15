class Solution {
    public int peakIndexInMountainArray(int[] A) {
        int m = Integer.MIN_VALUE;
        int res = -1;
        for(int i = 0; i < A.length; i++){
            if(A[i] > m){
                m = A[i];
                res = i;
            }
        }
        return res;
    }
}