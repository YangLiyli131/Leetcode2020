class Solution {
    public int[] sumEvenAfterQueries(int[] A, int[][] queries) {
        int[] res = new int[queries.length];
        int s = 0;
        for(int i : A){
            if(i % 2 == 0) s += i;
        }
        for(int i = 0; i < queries.length; i++){
            int val = queries[i][0];
            int idx = queries[i][1];
            
            if(Math.abs(A[idx]) % 2 == 0 && val % 2 != 0){
                s = s - A[idx];
            }else if(Math.abs(A[idx]) % 2 == 0 && val % 2 == 0){
                s += val;
            }else if(Math.abs(A[idx]) % 2 != 0 && val % 2 != 0){
                s += A[idx] + val;
            }
            A[idx] += val;
            res[i] = s;
        }
        return res;
    }
}