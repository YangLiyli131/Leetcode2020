class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> hm = new HashMap<>();
        for(String ss : strs){
            String s = helper(ss);
            if(!hm.containsKey(s)){
                List<String> temp = new ArrayList<>();
                temp.add(ss);
                hm.put(s,temp);
            }else{
                List<String> xx = hm.get(s);
                xx.add(ss);
                hm.put(s,xx);
            }
        }
        for(String x : hm.keySet()){
            res.add(hm.get(x));
        }
        return res;
    }
    private String helper(String s){
        char[] x = s.toCharArray();
        Arrays.sort(x);
        return new String(x);
    }
}