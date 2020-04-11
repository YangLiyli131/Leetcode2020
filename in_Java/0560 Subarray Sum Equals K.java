class Solution {
    public int subarraySum(int[] nums, int k) {
        if(nums == null || nums.length == 0) return 0;
        if(nums.length == 1){
            if(nums[0] == k) return 1;
            else return 0;
        }
        int res = 0;
        for(int i = 1; i < nums.length; i++){
            nums[i] = nums[i] + nums[i-1];
        }
        HashMap<Integer,Integer> hm = new HashMap<>();
        for(int i : nums){
            if(hm.containsKey(i - k)) res += hm.get(i-k);
            if(!hm.containsKey(i)) hm.put(i,1);
            else hm.put(i, hm.get(i)+1);
        }
        if(hm.containsKey(k)) res += hm.get(k);
        return res;
    }
}