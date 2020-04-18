class Solution {
    public String complexNumberMultiply(String a, String b) {
        String[] t1 = a.split("\\+");
        String[] t2 = b.split("\\+");
        String a1 = t1[0];
        String a2 = t1[1];
        String b1 = t2[0];
        String b2 = t2[1];
        
        int a_real;
        int a_img;
        int b_real;
        int b_img;
        if(a1.charAt(0) == '-'){
            a_real = -Integer.parseInt(a1.substring(1,a1.length()));
        }else{
            a_real = Integer.parseInt(a1);
        }
        if(b1.charAt(0) == '-'){
            b_real = -Integer.parseInt(b1.substring(1,b1.length()));
        }else{
            b_real = Integer.parseInt(b1);
        }
        if(a2.charAt(0) == '-'){
            a_img = -Integer.parseInt(a2.substring(1,a2.length()-1));
        }else{
            a_img = Integer.parseInt(a2.substring(0,a2.length()-1));
        }
        if(b2.charAt(0) == '-'){
            b_img = -Integer.parseInt(b2.substring(1,b2.length()-1));
        }else{
            b_img = Integer.parseInt(b2.substring(0,b2.length()-1));
        }
        int c = a_real * b_real - a_img * b_img;
        int d = a_real * b_img + a_img * b_real;
        return c + "+" + d + "i";
    }
}