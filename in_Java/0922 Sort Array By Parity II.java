class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int[] res = new int[A.length];
        int odd = 1;
        int even = 0;
        for(int i : A){
            if(i % 2 == 0){
                res[even] = i;
                even += 2;
            }else{
                res[odd] = i;
                odd += 2;
            }
        }
        return res;
    }
}