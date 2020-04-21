class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        if(coordinates.length == 2) return true;
        for(int i = 2; i < coordinates.length; i++){
            int x1 = coordinates[i-2][0];
            int y1 = coordinates[i-2][1];
            int x2 = coordinates[i-1][0];
            int y2 = coordinates[i-1][1];
            int x3 = coordinates[i][0];
            int y3 = coordinates[i][1];
            if((y3-y1)*(x2-x1) != (y2-y1)*(x3-x1)) return false;
        }
        return true;
    }
}