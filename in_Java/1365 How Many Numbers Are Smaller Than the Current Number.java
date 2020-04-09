class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] res = new int[nums.length];
        for(int i = 0; i < nums.length; i++) res[i] = nums[i];
        Arrays.sort(nums);
        Map<Integer,Integer> hm = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int cur = nums[i];
            if(!hm.containsKey(cur)){
                hm.put(cur,i);
            }
        }
        for(int i = 0; i < nums.length; i++){
            res[i] = hm.get(res[i]);
        }
        return res;
    }
}