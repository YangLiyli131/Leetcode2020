class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(arr);
        int minlen = Integer.MAX_VALUE;
        for(int i = 1; i < arr.length; i++){
            if(arr[i] - arr[i-1] < minlen) minlen = arr[i] - arr[i-1];
        }
        for(int i = 1; i < arr.length; i++){
            List<Integer> temp = new ArrayList<>();
            if(arr[i] - arr[i-1] == minlen){
                temp.add(arr[i-1]);
                temp.add(arr[i]);
                res.add(temp);
            }
        }
        return res;
    }
}