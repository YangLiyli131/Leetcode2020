class Solution {
    public int heightChecker(int[] heights) {
        int[] x = new int[heights.length];
        int res = 0;
        for(int i = 0; i < x.length; i++) x[i] = heights[i];
        Arrays.sort(x);
        for(int i = 0; i < x.length; i++){
            if(x[i] != heights[i]) res++;
        }
        return res;
    }
}