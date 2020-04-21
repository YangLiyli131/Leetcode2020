class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if(!wordList.contains(endWord)) return 0;
        
        HashMap<String,List<String>> adjL = new HashMap<>();
        
        List<String> t = new ArrayList<>();
        for(String s : wordList){
            if(dis(s,beginWord)) t.add(s);
        }
        adjL.put(beginWord,t);
        
        for(String s : wordList){
            t = new ArrayList<>();
            for(String ss : wordList){
                if(dis(s,ss)) t.add(ss);
            }
            adjL.put(s,t);
        }
        
        Set<String> hs = new HashSet<>();
        Queue<String> q = new LinkedList<>();
        q.add(beginWord);
        int level = 0;
        int n;
        while(q.size() != 0){
            n = q.size();
            level++;
            while(n -- != 0){
                String cur = q.poll();
                hs.add(cur);
                for(String nei: adjL.get(cur)){
                    if(nei.equals(endWord)) return level+1;
                    if(!hs.contains(nei)){
                        q.add(nei);
                        hs.add(nei);
                    }
                }   
            }
            
        }
        return 0;
        
    }
    private boolean dis(String a, String b){
        int dif = 0;
        for(int i = 0; i < a.length(); i++){
            if(a.charAt(i) != b.charAt(i)){
                dif++;
                if(dif > 1) return false;
            }
        }
        return dif == 1;
    }
}