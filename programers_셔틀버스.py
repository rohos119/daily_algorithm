# 2H 15M
# 문제정의 : 콘은 같은시각 도착한 크루보다 뒤에 서고, 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하라
# input : 1 n:운행횟수 10, 1 t:운행간격 60, 0 m:대기열에 도착하는시간 45, 1 timetable:크루가 오는시간 2000

# output : 0000 HH:MM 형식 2359, 제일 늦은 도착시간 

import datetime
from collections import *


def solution(n, t, m, timetable):
    answer = ''
    
    # logic
    # 버스는 n*m명을 태울 수 있으며, 최대 늦게 도착한 시간은 0900+n*t이다.
    # how...?
    # 자료 탐색을 어떻게 할것인가..?
    # 먼저 n*m명보다 줄선사람이 작을경우 콘은 그냥 맨뒤에 서면 되고, 마지막으로 탈수있는 시간에 타면된다.
    # 일단 input에서 제외해야될것을 판단
    # 23:59이면 무시, 00:00이면 타기위해 기다리는 것으로 판단 가능
    
    answer = 0
    # 모든 시간을 분으로 환산해서 생각
    # 예시: "09:10" => 9*60 + 10 = 550(분)
    # 크루 도착 시각 리스트
    crewTime = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crewTime.sort()
    # 버스 도착 시각 리스트
    busTime = [9*60 + t*i for i in range(n)]

    i = 0       # 다음에 버스에 오를 크루의 인덱스
    for tm in busTime:
      cnt = 0   # 버스에 타는 크루 수
      while cnt < m and i < len(crewTime) and crewTime[i] <= tm:
        i += 1
        cnt += 1
      # 버스에 자리가 남았을 경우
      if cnt < m: answer = tm
      # 버스에 자리가 없는 경우 맨 마지막 크루보다 1분 먼저 도착
      else: answer = crewTime[i - 1] - 1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
