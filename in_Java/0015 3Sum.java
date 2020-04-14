class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Set<List<Integer>> hs = new HashSet<>();
        int t;
        Map<Integer,Integer> hm;
        List<Integer> temp;
        for(int i = 0; i < nums.length; i++){
            t = -nums[i];
            hm = new HashMap<>();
            for(int j = 0; j < nums.length; j++){
                if(j == i) continue;
                if(!hm.containsKey(t - nums[j])) hm.put(nums[j], j);
                else{
                    temp = new ArrayList<>();
                    temp.add(-t);
                    temp.add(t - nums[j]);
                    temp.add(nums[j]);
                    Collections.sort(temp);
                    hs.add(temp);
                }
            }
        }
        for(List<Integer> i : hs) res.add(i);
        return res;
    }
}