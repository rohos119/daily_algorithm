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
        j, end = 0, len(matrix[0])-1
        while j < len(matrix):
            if target <= matrix[j][end]:
                if target in matrix[j]:
                    return True
                else:
                    return False
            else:
                j+=1
        return False
        # efficent way -> O(logm+logn) 
        # 시작점을 찾는거 -> logm / row 기준 바이너리 서치
        # 시작행에서 찾는거 -> logn / 행의 요소들로 바이너리 서치
        
        # # find start point 
        # m,n = len(matrix), len(matrix[0])
        # rp1,rp2 = 0,m-1
        # mid = (rp1+rp2)//2
        # if rp1 == rp2 :
        #     if target in matrix[rp1] :
        #         return True
        #     else :
        #         return False
        # while rp1 < rp2 :
        #     mid = (rp1+rp2)//2
        #     # 중간값에서 있으면 바로 종료
        #     if target in matrix[mid] :
        #         return True
        #     # 중간값에 없으면
        #     else :
        #         if n == 1 :
        #             if matrix[mid][0] < target :
        #                 rp1 =mid
        #             elif matrix[mid]
        #         else :
        #             if matrix[mid][-1] < target :
        #                 rp1 = mid
        #             elif matrix[mid][0] > target :
        #                 rp2 = mid
        #             else :
        #                 return False
        # return False