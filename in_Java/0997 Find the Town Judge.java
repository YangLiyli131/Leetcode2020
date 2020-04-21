class Solution {
    public int findJudge(int N, int[][] trust) {
        int[] indegree = new int[N];
        int[] outdegree = new int[N];
        for(int i = 0; i < trust.length; i++){
            int x = trust[i][0];
            int y = trust[i][1];
            outdegree[x-1]++;
            indegree[y-1]++;
        }
        for(int i = 0; i < N; i++){
            if(indegree[i] == N-1 && outdegree[i] == 0) return i+1;
        }
        return -1;
    }
}