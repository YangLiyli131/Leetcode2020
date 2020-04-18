class Solution {
    public String[] uncommonFromSentences(String A, String B) {
        List<String> L = new ArrayList<>();
        HashMap<String, Integer> hma = new HashMap<>();
        HashMap<String, Integer> hmb = new HashMap<>();
        for(String s : A.split(" ")){
            if(!hma.containsKey(s)) hma.put(s,1);
            else hma.put(s, hma.get(s)+1);
        }
        for(String s : B.split(" ")){
            if(!hmb.containsKey(s)) hmb.put(s,1);
            else hmb.put(s, hmb.get(s)+1);
        }
        for(String x : hma.keySet()){
            if(hma.get(x) == 1 && !hmb.containsKey(x)) L.add(x);
        }
        for(String x : hmb.keySet()){
            if(hmb.get(x) == 1 && !hma.containsKey(x)) L.add(x);
        }
        String[] res = new String[L.size()];
        int id = 0;
        for(String x : L) res[id++] = x;
        return res;
    }
}