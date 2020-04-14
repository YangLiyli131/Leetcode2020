class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        Map<String, Integer> hm1 = new HashMap<>();
        Map<String, Integer> hm2 = new HashMap<>();
        for(int i = 0; i < list1.length; i++){
            hm1.put(list1[i],i);
        }
        for(int i = 0; i < list2.length; i++){
            hm2.put(list2[i],i);
        }
        int cur = Integer.MAX_VALUE;
        int cursum;
        List<String> arr = new ArrayList<>();
        for(String k : hm1.keySet()){
            if(hm2.containsKey(k)){
                cursum = hm1.get(k) + hm2.get(k);
                if(cursum < cur){
                    cur = cursum;
                    arr = new ArrayList<>();
                    arr.add(k);
                }else if(cursum == cur){
                    arr.add(k);
                }else{
                    continue;
                }
            }
        }
        String[] res = new String[arr.size()];
        for(int i = 0; i < arr.size(); i++) res[i] = arr.get(i);
        return res;
    }
}