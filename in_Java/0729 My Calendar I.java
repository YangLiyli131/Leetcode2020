class MyCalendar {
    List<List<Integer>> base;
    public MyCalendar() {
        base = new ArrayList<>();
    }
    
    public boolean book(int start, int end) {
        List<Integer> cur = new ArrayList<>();
        cur.add(start); cur.add(end);
        if(base.size() == 0){
            base.add(cur);
            return true;
        }
        for(List<Integer> L : base){
            int a = L.get(0);
            int b = L.get(1);
            if(end <= a || start >= b) continue;
            else return false;
        }
        base.add(cur);
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */