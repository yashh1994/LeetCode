class Solution {
    public double findMedianSortedArrays(int[] num1, int[] num2) {
        int []ans = new int[num1.length+num2.length];
        int k=0,l=0,i=0;
        double an = 0;
        for(i = 0; i < num1.length+num2.length ; i++){
            if(k <= num1.length-1 && l <= num2.length-1){
                if(num2[l] >= num1[k]){
                    ans[i] = num1[k];
                    k++;
                   
                }else{
                    ans[i] = num2[l];
                    l++;
                   
                }
            }else{
                if(k < num1.length){
                    ans[i] = num1[k];
                    k++;
                }
                if(l < num2.length){
                     ans[i] = num2[l];
                    l++;
                }
            }
        }
        if(i%2==0){
            an = ans[i/2-1] + ans[i/2];
            an = an/2;
        }else{
            an = ans[(i/2)];
        }
        return an;
    }
}