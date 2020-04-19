public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        int id = 0;
        while(id < 32){
            int end = n & 1;
            n >>=1;
            res <<=1;
            res |= end;
            id++;
        }
        return res;
    }
}