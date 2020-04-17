class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int res = 0;
        int a = points[0][0];
        int b = points[0][1];
        for(int i = 1; i < points.length; i++){
            int x = points[i][0];
            int y = points[i][1];
            res += Math.max(Math.abs(x-a), Math.abs(y-b));
            a = x;
            b = y;
        }
        return res;
    }
}