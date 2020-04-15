class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[][] matrix = new int[numCourses][numCourses];
        int[] in_degree = new int[numCourses];
        for(int i = 0; i < prerequisites.length; i++){
            int pre = prerequisites[i][1];
            int now = prerequisites[i][0];
            if(matrix[pre][now] == 0) in_degree[now]++;
            matrix[pre][now] = 1;
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < numCourses; i++){
            if(in_degree[i] == 0) q.add(i);
        }
        int[] res = new int[numCourses];
        int id = 0;
        int count = numCourses;
        while(q.size() != 0){
            int cur = q.poll();
            res[id++] = cur;
            count--;
            for(int i = 0; i < numCourses; i++){
                if(matrix[cur][i] == 1){
                    in_degree[i]--;
                    if(in_degree[i] == 0) q.add(i);
                }
            }
        }
        if(count == 0) return res;
        else return new int[0];
    }
}