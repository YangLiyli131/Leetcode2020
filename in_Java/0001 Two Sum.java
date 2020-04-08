class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer,Integer> hm = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(!hm.containsKey(target - nums[i])){
                hm.put(nums[i],i);
            }else{
                res[0] = Math.min(i, hm.get(target - nums[i]));
                res[1] = Math.max(i, hm.get(target - nums[i]));
                break;
            }
        }
        return res;
    }
}