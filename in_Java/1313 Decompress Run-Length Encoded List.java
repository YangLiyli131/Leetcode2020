class Solution {
    public int[] decompressRLElist(int[] nums) {
        List<Integer> l = new ArrayList<>();
        for(int i = 0; i < nums.length-1; ){
            int a = nums[i];
            int b = nums[i+1];
            while(a-- != 0){
                l.add(b);
            }
            i += 2;
        }
        int[] res = new int[l.size()];
        for(int i = 0; i < res.length; i++){
            res[i] = l.get(i);
        }
        return res;
    }
}