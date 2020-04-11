class Solution {
    public int[] findErrorNums(int[] nums) {
        Map<Integer,Integer> hm = new HashMap<>();
        for(int i : nums){
            if(!hm.containsKey(i)) hm.put(i,1);
            else hm.put(i, hm.get(i)+1);
        }
        int[] res = new int[2];
        for(int i = 1; i <= nums.length; i++){
            if(!hm.containsKey(i)) res[1] = i;
            else{
                if(hm.get(i) == 2) res[0] = i;
            }
        }
        return res;
    }
}