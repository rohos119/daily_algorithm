# start 1100
# 문제정의 : 괄호를 회전하라
def solution(s):
    answer = 0
    temp = list(s)
    
    for _ in range(len(s)):
 
        st = []
        for i in range(len(temp)):
            if len(st) > 0:
                if st[-1] == '[' and temp[i] == ']':
                    st.pop()
                elif st[-1] == '(' and temp[i] == ')':
                    st.pop()
                elif st[-1] == '{' and temp[i] == '}':
                    st.pop()
                else:
                    st.append(temp[i])
            else:
                st.append(temp[i])
        if len(st) == 0:
            answer += 1
        temp.append(temp.pop(0))
 
    return answer
 
 
 
