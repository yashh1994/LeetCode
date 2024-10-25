import java.util.Arrays;

class Solution {
    boolean[][] visited;

    public int dfs(int[][] grid, int m, int n) {
        if (visited[m][n]) {
            return 0;
        }
        visited[m][n] = true;
        int ans = 1;
        if (m - 1 >= 0 && grid[m - 1][n] == 1 && !visited[m - 1][n]) {
            ans += dfs(grid, m - 1, n);
        }
        if (n - 1 >= 0 && grid[m][n - 1] == 1 && !visited[m][n - 1]) {
            ans += dfs(grid, m, n - 1);
        }
        if (m + 1 < grid.length && grid[m + 1][n] == 1 && !visited[m + 1][n]) {
            ans += dfs(grid, m + 1, n);
        }
        if (n + 1 < grid[0].length && grid[m][n + 1] == 1 && !visited[m][n + 1]) {
            ans += dfs(grid, m, n + 1);
        }
        return ans;
    }

    public int maxAreaOfIsland(int[][] grid) {
        visited = new boolean[grid.length][grid[0].length];
        int ans = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    ans = Math.max(ans, dfs(grid, i, j));
                }
            }
        }
        return ans;
    }
}
