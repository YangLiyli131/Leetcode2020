class Solution {
    public int maxDistToClosest(int[] seats) {
        List<Integer> seated = new ArrayList<>();
        for(int i = 0; i < seats.length; i++){
            if(seats[i] == 1) seated.add(i);
        }
        int dis = 0;
        for(int i = 0; i < seats.length; i++){
            if(seats[i] != 1){
                dis = Math.max(dis, helper(seated,i));
            }
        }
        return dis;
    }
    private int helper(List<Integer> L, int n){
        if(n < L.get(0)) return L.get(0) - n;
        if(n > L.get(L.size()-1)) return n - L.get(L.size()-1);
        int i = 0;
        while(i < L.size() && L.get(i) < n) i++;
        return Math.min(L.get(i) - n, n - L.get(i-1));
    }
}