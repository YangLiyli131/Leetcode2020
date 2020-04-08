class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer,Integer> hm = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int cur = nums[i];
            if(!hm.containsKey(cur)){
                hm.put(cur,i);
            }else{
                if(Math.abs(i - hm.get(cur)) <= k){
                    return true;
                }else{
                    hm.put(cur,i);
                }
            }
        }
        return false;
    }
}