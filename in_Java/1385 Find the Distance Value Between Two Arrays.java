class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int res = 0;
        boolean f;
        for(int i : arr1){
            f = true;
            for(int j : arr2){
                if(Math.abs(i - j) <= d){
                    f = false;
                    break;
                }
            }
            if(f) res++;
        }
        return res;
    }
}