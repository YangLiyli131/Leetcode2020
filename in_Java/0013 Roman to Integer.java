class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> hm = new HashMap<>();
        String[] arr1 = new String[]{"I","V","X","L","C","D","M","IV","IX","XL","XC","CD","CM"};
        int[] arr2 = new int[]{1,5,10,50,100,500,1000,4,9,40,90,400,900};
        for(int i = 0; i < arr1.length; i++){
            hm.put(arr1[i],arr2[i]);
        }
        int res = 0;
        for(int i = 0; i < s.length(); ){
            if(i+1 < s.length() && hm.containsKey(s.substring(i,i+2))){
                res += hm.get(s.substring(i,i+2));
                i += 2;
            }else{
                res += hm.get(s.substring(i,i+1));
                i++;
            }
        }
        return res;
    }
}