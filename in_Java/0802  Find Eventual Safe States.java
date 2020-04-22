class Solution {
    public static final int UNKNOWN = 0;  // unknown.
    public static final int UNSAFE = 1;   // unsafe
    public static final int SAFE   = 2;   // safe
    
    public List<Integer> eventualSafeNodes(int[][] graph) {
        List<Integer> res = new ArrayList<>();
        int[] states = new int[graph.length];
        for(int i = 0; i < graph.length; i++){
            if(dfs(graph, i, states)) res.add(i);
        }
        return res;
    }
    private boolean dfs(int[][] g, int i, int[] states){
        if(states[i] != UNKNOWN) return states[i] == SAFE;
        states[i] = UNSAFE;
        for(int nei : g[i]){
            if(!dfs(g,nei,states)) return false;
        }
        states[i] = SAFE;
        return true;
    }
}