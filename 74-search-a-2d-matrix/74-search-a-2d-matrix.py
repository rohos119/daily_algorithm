# start 0150 goal 40 end 
# 목표정의 : target이 Matrix안에 있는지
# input : m*n matrix -> 각 행은 오름차순 정렬, 각 row[n][0] < row[n][n] <row[n+1][0]
# output : false true
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # logic
        # target이 안에 있는지 어케 찾을래 ?
        
        # easy way ->  O(M*N)
        # row한개씩 돌면서 만약에 사이값일때 if in 하면 true, 아니면 for문 진행
        # 만약 다돌았는데 없으면 ? false
        # j, end = 0, len(matrix[0])-1
        # while j < len(matrix):
        #     if target <= matrix[j][end]:
        #         if target in matrix[j]:
        #             return True
        #         else:
        #             return False
        #     else:
        #         j+=1
        # return False
        # ----통과----그러나 효율성이 떨어짐
        
        # efficent way -> O(logm+logn) 
        # 시작점을 찾는거 -> logm / row 기준 바이너리 서치
        # 시작행에서 찾는거 -> logn / 행의 요소들로 바이너리 서치
        
        # 예외처리 
        if target < matrix[0][0] and target > matrix[-1][-1]:
            return False
        
        # find start row
        m,n = len(matrix), len(matrix[0])
        rp1,rp2 = 0,m-1
        mid = (rp1+rp2)//2
        while(rp1 <= rp2):
            mid = (rp1 + rp2)//2
            if (matrix[mid][0] <= target and target <= matrix[mid][n-1]):
                rp1 = rp2 = mid
                break
            elif (target < matrix[mid][0]):
                rp2 = mid - 1
            else:
                rp1 = mid + 1
        
        # set으로 matrix 바꿔서 big o 조금이라도 줄이는 방법
        # 이거 썼을때는 O(logm + n)
        # if rp1==rp2 :
        #     if target in matrix[rp1] :
        #         return True
        # else :
        #     if rp1<=0 and matrix[rp1][0] <= target and target <= matrix[rp1][n-1] :
        #         if target in set(matrix[rp1]) :
        #             return True
        #         else :
        #             return False
        #     elif rp2<m and matrix[rp2][0] <= target and target <= matrix[rp2][n-1] :
        #         if target in set(matrix[rp2]) :
        #             return True
        #         else :
        #             return False
        #     else :
        #         return False
        
        # 이렇게 하면 완벽한 o(logm + logn)
        top,bottom =rp1, rp2
        if (top == bottom):
            row = matrix[top]
        else:
            if (0 <= bottom) and (matrix[bottom][0] <= target <= matrix[bottom][n - 1]):
                row = matrix[bottom]
            elif (top < m) and (matrix[top][0] <= target <= matrix[top][n - 1]):
                row = matrix[top]
            else:
                return False
        
        # Find the target in the row
        L = 0
        R = n - 1
        while(L <= R):
            mid = (L + R) >> 1
            if (row[mid] == target):
                return True
            elif (row[mid] < target):
                L = mid + 1
            else:
                R = mid - 1
        
        return (0 <= L < n) and (row[L] == target)
            