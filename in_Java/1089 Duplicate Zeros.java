class Solution {
    public void duplicateZeros(int[] arr) {
        int czeros = 0;
        for(int i : arr){
            if(i == 0) czeros++;
        }
        int len = arr.length + czeros;
        for(int i = arr.length -1, j = len-1; i < j; i--,j--){
            if(arr[i] != 0){
                if(j < arr.length) arr[j] = arr[i];
            }else{
                if(j < arr.length) arr[j] = arr[i];
                j--;
                if(j < arr.length) arr[j] = arr[i];
            }
        }
    }
}