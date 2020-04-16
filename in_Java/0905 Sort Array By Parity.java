class Solution {
    public int[] sortArrayByParity(int[] A) {
        int[] res = new int[A.length];
        int i = 0;
        int j = res.length-1;
        for(int x : A){
            if(x % 2 == 0){
                res[i++] = x;
            }else{
                res[j--] = x;
            }
        }
        return res;
    }
}