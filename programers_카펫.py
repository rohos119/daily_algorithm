# start 2253 end 2312
# 문제정의 : 갈색 카펫개수와 노란카펫 개수를 보고 전체 가로세로 길이를 찾아라
# input : 1 brown 5*1e3 / 1 yellow 2*1e7 / w >= h 격자의 크기
# output : 가로,세로 크기 -> List

def solution(brown, yellow):
    total = brown + yellow
    # 카펫의 가로길이가 세로길이보다 크거나 같기 때문에 큰수에서 작은수로 반복
    for weight in range(total, 2, -1):
        if total % weight == 0: # 카펫넓이에서 가로길이 탐색
            height = total // weight # 카펫넓이 / 가로길이를 통해 세로길이 탐색
            # 구해진 카펫의 길이에서 테두리길이(2)만큼 빼주고 면적을 구한뒤 yellow의 면적과 같다면 해당 값 return
            if yellow == (weight-2) * (height-2):
                return [weight, height]
