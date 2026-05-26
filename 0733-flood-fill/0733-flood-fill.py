class Solution(object):
    def floodFill(self, image, sr, sc, color):
        initial_color = image[sr][sc]
        if initial_color == color:
            return image
            
        ROWS = len(image)
        COLS = len(image[0])
        stack = [(sr, sc)]
        
        while stack:
            r, c = stack.pop()
            if image[r][c] == initial_color:
                image[r][c] = color
                if r > 0: stack.append((r - 1, c))
                if r < ROWS - 1: stack.append((r + 1, c))
                if c > 0: stack.append((r, c - 1))
                if c < COLS - 1: stack.append((r, c + 1))
                
        return image
