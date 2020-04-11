class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        List<Integer> L = new ArrayList<>();
        for(int i = 0; i < nums.length; i++){
            L.add(index[i], nums[i]);
        }
        int[] res = new int[nums.length];
        for(int i = 0; i < res.length; i++) res[i] = L.get(i);
        return res;
    }
}