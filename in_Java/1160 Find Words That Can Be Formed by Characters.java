class Solution {
    public int countCharacters(String[] words, String chars) {
        HashMap<Character,Integer> hm = new HashMap<>();
        for(char c : chars.toCharArray()){
            if(!hm.containsKey(c)) hm.put(c,1);
            else hm.put(c, hm.get(c)+1);
        }
        int res = 0;
        for(String s : words){
            boolean f = true;
            HashMap<Character,Integer> t = new HashMap<>();
            for(char c : s.toCharArray()){
                if(!t.containsKey(c)) t.put(c,1);
                else t.put(c, t.get(c)+1);
            }
            for(char k : t.keySet()){
                if(!hm.containsKey(k)) {f = false;break;}
                else{
                    if(hm.get(k) < t.get(k)) {f = false;break;}
                }
            }
            if(f) res += s.length();
        }
        return res;
    }
}