class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(nums2 == null || nums2.length == 0 || n == 0) return;
        int id = m + n - 1; // index of where to insert
        // start from the end
        int i = m-1;
        int j = n-1;

        while(id >= 0 && i >= 0 && j >= 0){     
            //System.out.println(i);
            if(nums1[i] > nums2[j]){
                nums1[id] = nums1[i];
                i--;
            }else{
                nums1[id] = nums2[j];
                j--;
            }
            id--;
        }
        while(j >= 0){
            nums1[id--] = nums2[j--];
        }
    }
}