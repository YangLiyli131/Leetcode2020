class Solution {
    public int daysBetweenDates(String date1, String date2) {
        return Math.abs(date(date2) - date(date1));
    }
    private int date(String d){
        String[] ss = d.split("-");
        int a = Integer.parseInt(ss[0]);
        int b = Integer.parseInt(ss[1]);
        int c = Integer.parseInt(ss[2]);
        int res = 0;
        for(int i = 1971; i < a; i++){
            if(isLeap(i)) res += 366;
            else res += 365;
        }
        for(int i = 1; i < b; i++){
            if(i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12) res += 31;
            else if(i == 2 && isLeap(a)) res += 29;
            else if(i == 2) res += 28;
            else res += 30;
        }
        res += c;
        return res;
    }
    private boolean isLeap(int year){
        boolean leap = false;
        if(year % 4 == 0)
        {
            if( year % 100 == 0)
            {
                // year is divisible by 400, hence the year is a leap year
                if ( year % 400 == 0)
                    leap = true;
                else
                    leap = false;
            }
            else
                leap = true;
        }
        else
            leap = false;
        return leap;
    }
}