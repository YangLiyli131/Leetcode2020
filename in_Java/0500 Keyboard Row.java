class Solution {
    public String[] findWords(String[] words) {
        char[] r1 = new char[]{'q','w','e','r','t','y','u','i','o','p'};
        char[] r2 = new char[]{'a','s','d','f','g','h','j','k','l'};
        char[] r3 = new char[]{'z','x','c','v','b','n','m'};
        HashMap<Character,Integer> hm = new HashMap<>();
        for(char c : r1) hm.put(c,1);
        for(char c : r2) hm.put(c,2);
        for(char c : r3) hm.put(c,3);
        List<String> ar = new ArrayList<>();
        boolean f;
        for(String ss : words){
            String s = ss.toLowerCase();
            f = true;
            int rowid = hm.get(s.charAt(0));
            for(int i = 1; i < s.length(); i++){
                if(hm.get(s.charAt(i)) != rowid){
                    f = false;
                    break;
                }
            }
            if(f) ar.add(ss);
        }
        String[] res = new String[ar.size()];
        for(int i = 0; i < res.length; i++){
            res[i] = ar.get(i);
        }
        return res;
    }
}