class Solution {
    public double angleClock(int hour, int minutes) {
        double a = 30.0 * hour + minutes/2.0;
        double b = 6.0 * minutes;
        double c = Math.abs(a - b);
        return Math.min(c, 360.0 - c);
    }
}