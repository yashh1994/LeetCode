class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        StringBuilder s1 = new StringBuilder();
        int i;
        for(i = 0; num1.charAt(i) != '+'; i++) {
            s1.append(num1.charAt(i));
        }
        int r1 = Integer.parseInt(s1.toString());
        int i1 = Integer.parseInt(num1.substring(i + 1, num1.length() - 1));

        s1.setLength(0);
        for(i = 0; num2.charAt(i) != '+'; i++) {
            s1.append(num2.charAt(i));
        }
        int r2 = Integer.parseInt(s1.toString());
        int i2 = Integer.parseInt(num2.substring(i + 1, num2.length() - 1));

        int real = (r1 * r2) + (-1 * i1 * i2);
        int image = (r1 * i2) + (r2 * i1);
        String ans = String.format("%d+%di", real, image);
        return ans;
    }
}
