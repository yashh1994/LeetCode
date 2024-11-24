class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0
        min_abs = float('inf')
        neg_count = 0
        
        for row in matrix:
            for x in row:
                min_abs = min(min_abs, abs(x))
                if x < 0:
                    total_sum -= x  
                    neg_count += 1
                else:
                    total_sum += x  
        
        if neg_count % 2 == 1:
            return total_sum - 2 * min_abs
        return total_sum
