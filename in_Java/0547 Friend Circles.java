class Solution {
    public int findCircleNum(int[][] M) {
        int num_nodes = M.length;
        int res = 0;
        boolean[] visited = new boolean[num_nodes];
        Stack<Integer> st = new Stack<>();
        int cur;
        for(int i = 0; i < num_nodes; i++){
            if(!visited[i]){
                res++;
                st.push(i);
                while(!st.isEmpty()){
                    cur = st.pop();
                    visited[cur] = true;
                    for(int j = 0; j < M[0].length; j++){
                        if(j != cur && M[cur][j] == 1){
                            if(!visited[j]) st.push(j);
                        }
                    }
                }
            }
        }
        return res;
    }
}