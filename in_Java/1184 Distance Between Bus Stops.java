class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        int n = 0;
        int nn = 0;
        for(int i : distance) n += i;
        int a = Math.min(start,destination);
        int b = Math.max(start, destination);
        for(int i = a; i < b; i++){
            nn += distance[i];
        }
        return Math.min(nn, n - nn);
    }
}