import java.util.HashSet;
import java.util.Set;

class Solution {
    
    private int distanceSquared(int[] p1, int[] p2) {
        return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]);
    }

    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[][] points = {p1, p2, p3, p4};
        Set<Integer> distances = new HashSet<>();

        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                distances.add(distanceSquared(points[i], points[j]));
            }
        }
        return distances.size() == 2 && !distances.contains(0);
    }
}
