class Solution {
    public int countLargestGroup(int n) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        int cur;
        for(int i = 1; i <= n; i++){
            cur = disum(i);
            if(!hm.containsKey(cur)) hm.put(cur,1);
            else hm.put(cur, hm.get(cur)+1);
        }
        int res = 0;
        for(int i : hm.values()){
            if(i > res) res = i;
        }
        int answer = 0;
        for(int i : hm.values()){
            if(i == res) answer++;
        }
        return answer;
    }
    private int disum(int n){
        int res = 0;
        while(n != 0){
            res += n % 10;
            n /= 10;
        }
        return res;
    }
}