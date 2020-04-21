class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if(image[sr][sc] == newColor) return image;
        dfs(image, sr, sc, image[sr][sc], newColor);
        return image;
    }
    private void dfs(int[][] image, int sr, int sc, int c, int nc){
        if(sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length || image[sr][sc] != c) return;
        image[sr][sc] = nc;
        dfs(image, sr-1, sc,c,nc);
        dfs(image, sr+1, sc,c,nc);
        dfs(image, sr, sc+1,c,nc);
        dfs(image, sr, sc-1,c,nc);
    }
}