class Solution {
    public String convert(String s, int numRows) {
       if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            rows.add(new StringBuilder());
        }
        int cur = 0;
        boolean check = false;
        for(char c : s.toCharArray()){
            rows.get(cur).append(c);
            if(cur == 0 || cur == numRows-1){
                check = !check;
            }
            cur += check?1:-1;
        }
        StringBuilder ans = new StringBuilder();
        for(StringBuilder b : rows){
            ans.append(b);
        }
        return ans.toString();
    }
}