class Solution {
    public int[] plusOne(int[] digits) {
        int L = digits.length;
        int overflow = 0;
        digits[L-1] += 1;
        for(int i = L-1; i >= 0; i--){
            digits[i] += overflow;
            int cur = digits[i];
            if(cur < 10){
                overflow = 0;
                break;
            }else{
                digits[i] = 0;
                overflow = 1;
            }
        }
        if(overflow == 1){
            int[] res = new int[digits.length+1];
            res[0] = 1;
            for(int i = 1; i < res.length; i++){
                res[i] = digits[i-1];
            }
            return res;
        }else{
            return digits;
        }
    }
}