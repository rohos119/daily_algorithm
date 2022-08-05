# start : 1133 goal 1200
# definition : 2글자인 words 리스트에서 가장 긴 회문을 만들어서 길이를 반환해라
# input : 1 word 1e5
# output : longest length
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
#         # logic 
#         # 탐색은 어떻게 할건지?
#         # brute force ?
#         # 일단 회문이 될 가능성이 높은 게 뭔지 생각해보자
#         # 대칭인 두 쌍을 찾자, 쌍이 여러개면 -> 붙여~
#         # 회문 중간에 대칭문 이 있어도 되니 대칭도 포함
        
#         pos,don = 0,[]
#         pos2 = []
#         while words :
#             w = words.pop()
#             if w == w[::-1] :
#                 if w in don :
#                     don[don.index(w)] +=w
#                 else :
#                     don.append(w)
#             else :
#                 for t in words :
#                     if t == w[::-1]:
#                         pos2.append([w,t])
#                         pos+=4
#         print(pos2,don)
#         n = len(don)
        
#         # 전부 해당사항 없을때
#         if pos==0 and n == 0 :
#             return 0
#         elif pos==0 and n>0 :
#             # don에서 같은 문자가 있을 경우 회문을 만들 수 있음
#             print(don)
#             c = 0
#             while don :
#                 x =len(don.pop())
#                 if x > c :
#                     c=x
#             return c
#         elif pos >0 and n==0 :
#             return pos
#         else :
#             c = 0
#             while don :
#                 x =len(don.pop())
#                 if x > c :
#                     c=x
#             return c+pos
      cntr = Counter(words)
      npairs = 0
      addtwo = False
      
      for i in cntr:
        # aa 문자 존재 시
        if i[0] == i[1]:
          # 하나라도 남으면 addtwo 추가
          if cntr[i]%2 == 1:
            addtwo = True
          if cntr[i] > 1:
            M = cntr[i]//2
            npairs += M*4
            cntr[i] -= M*2
        else:
          if i[::-1] in cntr.keys():
            if cntr[i] > 0 and cntr[i[::-1]] > 0:
              M = min(cntr[i], cntr[i[::-1]])
              npairs += M*4
              cntr[i] -= M*1
              cntr[i[::-1]] -= M*1

      if addtwo:
        npairs += 2

      return npairs
