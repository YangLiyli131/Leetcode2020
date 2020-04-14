class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> hs = new HashSet<>();
        for(int i : nums1) hs.add(i);
        List<Integer> arr = new ArrayList<>();
        for(int i : nums2){
            if(hs.contains(i)){
                arr.add(i);
                hs.remove(i);
            }
        }
        int[] res = new int[arr.size()];
        for(int i = 0; i < arr.size(); i++) res[i] = arr.get(i);
        return res;
    }
}