# start 1816 end 1847
# 문제정의 : 오른손 # 엄지 * ->  왼손 1,4,7 오른손 3 6 9 가운데 2,5,8,0 가운데는 가까운 손이 입력
# 만약 거리가 같으면 오른손잡이는 엄지, 왼손잡이는 왼손으로 키패드를 눌러라
# input : 1 numbers 1000 / hand left right
# output : LR로 구성된 리스트
def solution(number, hand):
    
    # logic
    # 키패드를 배열 index로 접근하게 만들어서 거리 계산을 하자
    # 왼손 1,4,7 / 오른손 3,6,9 움직이는 것을 default 로 두고
    keypad = { 1: (0,0), 2: (0,1),3: (0,2),
             4: (1,0),5: (1,1),6: (1,2),
             7: (2,0),8: (2,1),9: (2,2),
             '*': (3,0),0: (3,1),'#': (3,2)}
    
    default = {1:'L',4:'L',7:'L',3:'R',6:'R',9:'R'}
    answer = []
    rp, lp = (3,0),(3,2)
    for n in number :
        if n not in default.keys() :
            x,y = keypad[n]
            rd,ld = abs(x-rp[0])+abs(y-rp[1]), abs(x-lp[0])+abs(y-lp[1])
            if rd < ld :
                answer.append('R')
                rp = (x,y)
            elif rd==ld: 
                if hand =='right' :
                    answer.append('R')
                    rp = (x,y)
                else :
                    answer.append('L')
                    lp = (x,y)
            else :
                answer.append('L')
                lp = (x,y)
        else :
            answer.append(default[n])
            if default[n] =='R':
                rp = keypad[n]
            else :
                lp = keypad[n]

    return ''.join(answer)
