class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer,Integer> hm = new HashMap<>();
        for(int i : nums1){
            if(!hm.containsKey(i)) hm.put(i,1);
            else hm.put(i, hm.get(i)+1);
        }
        List<Integer> arr = new ArrayList<>();
        for(int i : nums2){
            if(hm.containsKey(i) && hm.get(i) > 0){
                arr.add(i);
                hm.put(i, hm.get(i)-1);
            }
        }
        int[] res = new int[arr.size()];
        for(int i = 0; i < arr.size(); i++) res[i] = arr.get(i);
        return res;
    }
}