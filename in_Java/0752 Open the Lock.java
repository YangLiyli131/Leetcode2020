class Solution {
    public int openLock(String[] deadends, String target) {
        // create a graph with 10000 nodes, from 0000 to 9999
        // edges exist between nodes that differ by 1 digit slot
        // BFS to find shortest path
        // if come across deadends, skip it and continue;
        if(target.equals("0000")) return 0;
        List<String> death = new ArrayList<>();
        for(String x : deadends) death.add(x);
        if(death.contains("0000")) return -1;
        
        // pay attention to cycles in graph
        Set<String> visited = new HashSet<>();
        visited.add("0000");
        Queue<String> q = new LinkedList<>();
        q.add("0000");
        int level = 0;
        int len;
        String thisone;
        while(q.size() != 0){
            len = q.size();
            while(len-- != 0){
                thisone = q.poll();
                //if(death.contains(thisone)) continue;
                if(thisone.equals(target)) return level;
                StringBuilder sb = new StringBuilder(thisone);
                for(int id = 0; id < 4; id++){
                    char c = sb.charAt(id);
                    String s1 = sb.substring(0,id) + (c == '9'? 0 : c - '0' + 1) + sb.substring(id+1,4);
                    String s2 = sb.substring(0,id) + (c == '0'? 9 : c - '0' - 1) + sb.substring(id+1,4);
                    if(!visited.contains(s1) && !death.contains(s1)){
                        q.add(s1);
                        visited.add(s1);
                    }
                    if(!visited.contains(s2) && !death.contains(s2)){
                        q.add(s2);
                        visited.add(s2);
                    }
                }                      
            }
            level++;
        }
        return -1;
    }
}