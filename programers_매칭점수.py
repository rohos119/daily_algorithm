# start 1622
# 문제정의 : 페이지 내에서 검색어 빈도수인 기본점수, 해당 웹페이지에서 링크가 걸린 곳의 기본점수의 합//외부링크 수인 링크점수의
#           합산인 매칭점수를 구하여라
# input : 검색어 word, html pages
# output : 매칭점수가 가장 높은 index를 구하여라 -> 웹페이지가 여러개면 가장 작은 index

import re

def solution(word, pages):
    # logic
    # 기본점수는 -> <body> 테그값 확인
    # 링크점수 -> <meta property="org:url"> 태그값 확인
    # dictionary type으로 정의해서 기본점수 값을 저장하자 key 는 url
    page_dic = {}
    answer = 0
    for p in pages :
        url = re.search('<meta property="og:url" content="(\S+)"', p).group(1)
        n_point = 0
        for f in re.findall(r'[a-zA-Z]+', p.lower()):
            if f == word.lower():
                n_point += 1
        link_url = re.findall('<a href="(https://[\S]*)"', p)
        page_dic[url]= {'n_point' : n_point, 'link_url' : link_url }
    
    answer = []
    for idx,page in enumerate(page_dic) :
        l_point = 0
        print(page,page_dic[page]['link_url'])
        for link in page_dic[page]['link_url'] :
            if link in page_dic :
                l_point += page_dic[link]['n_point']/len(page_dic[page]['link_url'])
                print(page,link,l_point,page_dic[link]['n_point'],len(page_dic[page]['link_url']))
        answer.append([idx, page_dic[page]['n_point']+l_point])
    
    print(answer)
    answer = sorted(answer, key= lambda x:-x[1])
    return answer[0][0]
