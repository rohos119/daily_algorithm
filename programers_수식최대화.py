import re
def solution(expression):
    priority = [ ['*','+','-'],['*','-','+'],
                 ['+','*','-'],['+','-','*'],
                 ['-','+','*'],['-','*','+'],]
    split =[]
    number =''
    for t in enumerate(expression) :
        if t[1] =='*' or t[1]=='-' or t[1]=='+' :
            split.append(number)
            split.append(t[1])
            number=''
        else :
            number += t[1]
            if t[0] == len(expression)-1:
                split.append(number)
            

    temp=split.copy()
    cacul=[]
    answer=[]
    for prior in priority :
        for p in prior :
            for t in enumerate(temp) :
                if t[1] == p :
                    x=cacul.pop()
                    y=temp.pop(t[0]+1)
                    if t[1] =='-' :
                        cacul.append(int(x)-int(y))
                    elif t[1]=='*':
                        cacul.append(int(x)*int(y))
                    elif t[1]=='+' :
                        cacul.append(int(x)+int(y))
                else :    
                    cacul.append(t[1])
            temp = cacul
            cacul=[]
        answer.append(abs(temp[0]))
        temp = split.copy()
    
    return max(answer)
