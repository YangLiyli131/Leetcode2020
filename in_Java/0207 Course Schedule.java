class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[][] matrix = new int[numCourses][numCourses];
        int[] incoming_degree = new int[numCourses];
        for(int i = 0; i < prerequisites.length; i++){
            int pre = prerequisites[i][1];
            int cur = prerequisites[i][0];
            if(matrix[pre][cur] == 0) incoming_degree[cur]++;
            matrix[pre][cur] = 1;
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < numCourses; i++){
            if(incoming_degree[i] == 0) q.add(i);
        }
        int count = numCourses;
        // now queue contains nodes with no incoming edges
        while(q.size()!= 0){
            int now = q.poll();
            count--;
            for(int i = 0; i < numCourses; i++){
                if(matrix[now][i] != 0){
                    incoming_degree[i]--;
                    if(incoming_degree[i] == 0) q.add(i);
                }
            }
        }
        return count == 0;
    }
}