class Solution {
    public int rotatedDigits(int N) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        hm.put(1,1);hm.put(0,0); hm.put(8,8); hm.put(2,5);
        hm.put(5,2);hm.put(6,9); hm.put(9,6);
        int res = 0;
        boolean able = true;
        for(int i = 1; i <= N; i++){
            int back = i;
            int cur = 0;
            int power = 0;
            while(i != 0){
                int t = i % 10;
                i /= 10;
                if(!hm.containsKey(t)){
                    able = false;
                    break;
                }else{
                    cur += hm.get(t) * Math.pow(10,power);
                    able = true;
                    power++;
                }
            }
            if(able && cur != back) res++;
            i = back;
        }
        return res;
    }
}