class Solution:

## DFS    
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         m = len(image)
#         n = len(image[0])
        
#         def valid(x, y):
#             if 0 <= x < m and 0 <= y < n:
#                 return True
#             return False
        
#         def fill(i, j, match_color, fill_color):
#             if not valid(i, j) or image[i][j] != match_color:
#                 return
#             image[i][j] = fill_color
#             for nx, ny in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
#                 fill(nx, ny, match_color, fill_color)
                    
#         match_color = image[sr][sc]
#         if match_color == color:
#             return image
#         fill(sr, sc, match_color, color)
#         return image

## BFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

            h, w = len(image), len(image[0])

            src_color = image[sr][sc]

            traversal_queue = deque( [(sr, sc)] )

            while traversal_queue:

                cur_r, cur_c = traversal_queue.popleft()

                if cur_r < 0 or cur_r >= h or cur_c < 0 or cur_c >= w or image[cur_r][cur_c] == newColor  or image[cur_r][cur_c] != src_color:
                    continue

                # update color
                image[cur_r][cur_c] = newColor


                # BFS to 4-connected neighbors
                traversal_queue.append( (cur_r-1, cur_c) )
                traversal_queue.append( (cur_r+1, cur_c) )
                traversal_queue.append( (cur_r, cur_c-1) )
                traversal_queue.append( (cur_r, cur_c+1) )

            return image