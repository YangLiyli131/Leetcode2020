class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] temp = new int[amount+1];
        int cur;
        boolean found;
        for(int i = 1; i < amount+1; i++){
            found = false;
            cur = Integer.MAX_VALUE;
            for(int x : coins){
                if(i % x == 0){
                    cur = i / x < cur? i/x : cur;
                    found = true;
                }
                if(i - x >= 0 && temp[i-x] != -1){
                    found = true;
                    if(temp[i-x]+1 < cur) cur = temp[i-x]+1;
                }
            }
            if(!found) temp[i] = -1;
            else temp[i] = cur;
        }
        //for(int i : temp) System.out.println(i);
        return temp[amount];
    }
}