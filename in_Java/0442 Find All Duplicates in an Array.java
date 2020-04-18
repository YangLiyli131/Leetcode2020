class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        // first round
        // find elements appeared twice and also elements not appeared
        List<Integer> res = new ArrayList<>();       
        for(int i = 0; i < nums.length; i++){
            int cur = Math.abs(nums[i]);
            nums[cur-1] = -nums[cur-1];
        }
        for(int i = 0; i < nums.length; i++){
            if(nums[i] > 0) res.add(i+1);
        }
        
        // restore input array
        for(int i = 0; i < nums.length; i++){
            if(nums[i] < 0) nums[i] = -nums[i];
        }
        // remove elements not show in the array from final result
        for(int i = 0; i < nums.length; i++){
            int cur = Math.abs(nums[i]);
            if(nums[cur-1] > 0) nums[cur-1] = -nums[cur-1];
        }
        for(int i = 0; i < nums.length; i++){
            if(nums[i] > 0) res.remove(res.indexOf(i+1));
        }      
        return res;
    }
}