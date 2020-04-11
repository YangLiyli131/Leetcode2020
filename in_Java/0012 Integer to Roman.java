class Solution {
    public String intToRoman(int num) {
        Map<Integer,String> hm = new HashMap<>();
        String[] arr1 = new String[]{"I","V","X","L","C","D","M","IV","IX","XL","XC","CD","CM"};
        int[] arr2 = new int[]{1,5,10,50,100,500,1000,4,9,40,90,400,900};
        for(int i = 0; i < arr1.length; i++){
            hm.put(arr2[i],arr1[i]);
        }
        Map<Integer, int[]> hm2 = new HashMap<>();
        hm2.put(1, new int[]{1});
        hm2.put(2, new int[]{1,1});
        hm2.put(3, new int[]{1,1,1});
        hm2.put(4, new int[]{4});
        hm2.put(5, new int[]{5});
        hm2.put(6, new int[]{5,1});
        hm2.put(7, new int[]{5,1,1});
        hm2.put(8, new int[]{5,1,1,1});
        hm2.put(9, new int[]{9});
        
        String res = "";
        String cur;
        int t;
        int id = 0;
        int idx;
        while(num != 0){
            t = num % 10;
            if(t == 0){
                num /= 10;
                id++;
                continue;
            }
            int[] x = hm2.get(t);
            cur = "";
            for(int i : x){
                //System.out.println(i);
                idx = (int)(i * Math.pow(10,id));
                cur += hm.get(idx);
            }
            res = cur + res;
            num /= 10;
            id++;
        }
        return res;
    }
}