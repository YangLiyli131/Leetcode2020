/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     public int f(int x, int y);
 * };
 */

class Solution {
    public List<List<Integer>> findSolution(CustomFunction customfunction, int z) {
        List<List<Integer>> res = new ArrayList<>();
        int i = 1;
        int j = 1000;
        while(i <= 1000 && j > 0){
            int x = customfunction.f(i,j);
            if(x > z) j--;
            else if(x < z) i++;
            else{
                List<Integer> t = new ArrayList<>();
                t.add(i++);t.add(j--);
                res.add(t);
            }
        }
        return res;
    }
}