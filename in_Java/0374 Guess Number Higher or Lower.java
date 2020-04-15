/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return       -1 if num is lower than the guess number
 *                1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int i = 1; 
        int j = n;
        while(i <= j){
            int m = i + (j-i)/2;
            if(guess(m) == 0) return m;
            else if(guess(m) == 1) i = m + 1;
            else j = m-1;
        }
        return -1;
    }
}