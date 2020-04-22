class Solution {
    public String reformat(String s) {
        int num_c = 0;
        int num_n = 0;
        for(char c : s.toCharArray()){
            if(c >= 'a' && c <= 'z') num_c++;
            else num_n++;
        }
        if(Math.abs(num_c - num_n) > 1) return "";
        char[] res = new char[num_c + num_n];
        char[] allchar = new char[num_c];
        char[] allnum = new char[num_n];
        int i = 0, j = 0;
        for(char c : s.toCharArray()){
            if(c >= 'a' && c <= 'z') allchar[i++] = c;
            else allnum[j++] = c;
        }
        int c_id = 0, n_id = 0, id = 0;
        if(num_c > num_n){
            res[id++] = allchar[c_id++];
            while(id < res.length){
                res[id++] = allnum[n_id++];
                res[id++] = allchar[c_id++];
            }
        }else if(num_c < num_n){
            res[id++] = allnum[n_id++];
            while(id < res.length){
                res[id++] = allchar[c_id++];
                res[id++] = allnum[n_id++];
            }
        }else{
            while(id < res.length){
                res[id++] = allchar[c_id++];
                res[id++] = allnum[n_id++];
            }
        }
        return String.valueOf(res);
    }
}