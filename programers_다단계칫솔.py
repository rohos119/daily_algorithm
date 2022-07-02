def solution(enroll, referral, seller, amount):
    
    answer = [0]*len(enroll)
    visit = [0]*len(enroll)
    
    # BigO(n^2) 
    # why ? seller -> n * enroll.index -> n 
    
    # 그럼 기본 seller와 reffer사이의 구조를 바꾸자... how? dic?
    # yes dic! dic은 index 값을 찾는데 O(1), list.index는 O(N)
    
    enroll_dic = {}
    for i in range(len(enroll)) :
        enroll_dic[enroll[i]] = i

    for i,s in enumerate(seller) :
        profit = amount[i]*100
        while s != '-' and profit >0 :
            idx = enroll_dic[s]
            up_profit = profit//10
            answer[idx] += profit-up_profit
            profit = up_profit
            s = referral[idx]
        
    return answer
