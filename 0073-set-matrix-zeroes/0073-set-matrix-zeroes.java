class Solution {
    public void setZeroes(int[][] matrix) {
        List<Integer> is = new ArrayList<>();
        List<Integer> js = new ArrayList<>();
        int row = matrix.length;
        int col = matrix[0].length;
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                if(matrix[i][j] == 0){
                    js.add(j);
                    is.add(i);
                }
            }
        }

        for(int k = 0; k < is.size(); k++){
            int i = is.get(k);
            int j = js.get(k);
            for(int r = 0; r < col; r++){
                matrix[i][r] = 0;
            }
            for(int r = 0; r < row; r++){
                matrix[r][j] = 0;
            }
        }
    }
}