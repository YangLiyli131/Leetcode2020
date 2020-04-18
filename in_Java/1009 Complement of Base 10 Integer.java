class Solution {
    public int bitwiseComplement(int N) {
        if(N == 0) return 1;
        int res = 0;
        int p = 0;
        int t;
        while(N != 0){
            t = N % 2;
            if(t == 0){
                res += Math.pow(2,p);
            }
            p++;
            N /= 2;
        }
        return res;
    }
}