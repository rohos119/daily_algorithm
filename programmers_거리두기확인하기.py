def solution(places):
    answer = []

    def check(place):
        temp = []
        for i, r in enumerate(place):
            for j, c in enumerate(r):
                if c == 'P': temp.append((i, j))
        if len(temp) ==0 :
            return 1
        start = temp.pop(0)
        while temp:
            for t in temp:
                x_dist =start[0] - t[0]
                y_dist =start[1] - t[1]
                if abs(x_dist) + abs(y_dist) < 2:
                    return 0
                elif abs(x_dist) + abs(y_dist) == 2:
                    x = min(start, t)
                    if x_dist > 0 and y_dist > 0 and (place[x[0]+1][x[1]] =='O' or place[x[0]][x[1]+1] =='O' )  :
                        return 0
                    if x_dist > 0 and y_dist ==0 and place[x[0]+1][x[1]] =='O' :
                        return 0
                    if y_dist > 0 and x_dist ==0 and place[x[0]][x[1]+1] =='O' :
                        return 0
            start = temp.pop(0)
        return 1

    for r in places:
        answer.append(check(r))
    return answer
