class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        int[] visited = new int[n];
        Stack<Integer> st = new Stack<>();
        int cur;
        st.push(0);               
        while(!st.isEmpty()){
            cur = st.pop();
            visited[cur] = 1;
            for(int j : rooms.get(cur)){
                if(visited[j] == 0){
                    st.push(j);
                }
            }
        }
        int res = 0;
        for(int i : visited) res += i;
        return res == n;
    }
}