class Solution {
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length == 0) return 0;
        int curmin = prices[0];
        int res = Integer.MIN_VALUE;
        int[] t = new int[prices.length];
        for(int i = 1; i < prices.length; i++){
            if(prices[i] >= curmin){
                t[i] = prices[i] - curmin;
            }else{
                curmin = prices[i];
                t[i] = 0;
            }
        }
        for(int i : t){
            if(i > res) res = i;
        }
        return res;
    }
}