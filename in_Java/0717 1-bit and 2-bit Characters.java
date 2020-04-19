class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i;
        for(i = 0; i < bits.length-1; ){
            if(bits[i] == 1) i += 2;
            else i++;
        }
        return i == bits.length-1;
    }
}