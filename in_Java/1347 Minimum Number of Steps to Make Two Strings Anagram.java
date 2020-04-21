class Solution {
    public int minSteps(String s, String t) {
        Map<Character,Integer> hm1 = new HashMap<>();
        Map<Character,Integer> hm2 = new HashMap<>();
        for(char c : s.toCharArray()){
            if(!hm1.containsKey(c)) hm1.put(c,1);
            else hm1.put(c, hm1.get(c)+1);
        }
        for(char c : t.toCharArray()){
            if(!hm2.containsKey(c)) hm2.put(c,1);
            else hm2.put(c, hm2.get(c)+1);
        }
        int res = 0;
        for(char k : hm1.keySet()){
            if(!hm2.containsKey(k)) res += hm1.get(k);
        }
        for(char k : hm2.keySet()){
            if(hm1.containsKey(k) && hm1.get(k) > hm2.get(k)) res += hm1.get(k) - hm2.get(k);
        }
        return res;
    }
}