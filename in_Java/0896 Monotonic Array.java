class Solution {
    public boolean isMonotonic(int[] A) {
        int p = 1;
        while(p < A.length && A[p] == A[0]) p++;
        if(p == A.length) return true;
        boolean increase = A[p] > A[0];
        boolean decrease = A[p] < A[0];
        for(int i = 1; i < A.length; i++){
            if(increase && A[i] < A[i-1]) return false;
            if(decrease && A[i] > A[i-1]) return false;
        }
        return true;
    }
}