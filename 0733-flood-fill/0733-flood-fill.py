class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(image,row,col):
            image[row][col] = color
            for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                r,c = row+x,col+y
                if 0<=r<len(image) and 0 <= c < len(image[0]) and image[r][c] == original_color:
                    bfs(image,r,c)
        original_color = image[sr][sc]
        if original_color == color:
            return image
        bfs(image,sr,sc)
        return image
            

        