class Solution {
    public int[] replaceElements(int[] arr) {
        int curmax = arr[arr.length-1];
        arr[arr.length-1] = -1;
        int t;
        for(int i = arr.length-2; i >= 0; i--){
            t = arr[i];
            arr[i] = curmax;
            if(t > curmax) curmax = t;
        }
        return arr;
    }
}