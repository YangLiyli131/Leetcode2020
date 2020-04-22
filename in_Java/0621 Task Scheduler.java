class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        int maxcount = 0;
        int maxfreq = 0;
        for(char c : tasks){
            count[c-'A']++;
            if(maxcount == count[c-'A']) maxfreq++;
            if(maxcount < count[c-'A']){
                maxcount = count[c-'A'];
                maxfreq = 1;
            }
        }
        int partCount = maxcount - 1;
        int emptySlots = partCount * (n - maxfreq + 1);
        int available_tasks = tasks.length - maxfreq * maxcount;
        int idles = Math.max(0, emptySlots - available_tasks);
        return idles + tasks.length;
    }
}