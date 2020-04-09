class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer,Integer> hm = new HashMap<>();
        for(int i : arr){
            if(!hm.containsKey(i)) hm.put(i,1);
            else hm.put(i,hm.get(i)+1);
        }
        Set<Integer> hs = new HashSet<>();
        for(int i : hm.values()){
            if(!hs.contains(i)) hs.add(i);
            else return false;
        }
        return true;
    }
}