class Solution {
    public boolean isAnagram(String s, String t) {
        if(s == null && t == null) return true;
        if(s == null || t == null) return false;
        if(s.length() != t.length()) return false;
        HashMap<Character,Integer> hm = new HashMap<>();
        for(char c : s.toCharArray()){
            if(!hm.containsKey(c)){
                hm.put(c,1);
            }else{
                hm.put(c,hm.get(c)+1);
            }
        }
        for(char c : t.toCharArray()){
            if(!hm.containsKey(c)){
                return false;
            }else{
                hm.put(c,hm.get(c)-1);
            }
        }
        for(char k : hm.keySet()){
            if(hm.get(k) != 0) return false;
        }
        return true;
    }
}