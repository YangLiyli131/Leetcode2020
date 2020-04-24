class Solution {
    public int numTeams(int[] rating) {
        int res = 0;
        if(rating.length < 3) return res;
        for(int j = 0; j < rating.length-1; j++){
            int leftSmaller = 0, leftLarger = 0;
            int rightSmaller = 0, rightLarger = 0;
            for(int i = 0; i < j; i++){
                if(rating[i] < rating[j]) leftSmaller++;
                if(rating[i] > rating[j]) leftLarger++;
            }
            for(int k = j+1; k < rating.length; k++){
                if(rating[k] > rating[j]) rightLarger++;
                if(rating[k] < rating[j]) rightSmaller++;
            }
            res += leftSmaller * rightLarger + leftLarger * rightSmaller;
        }
        return res;
    }
}