def hanoi(src, thr, dst, answer, n):
    if n == 1:
        answer.append([src, dst])
        return
    hanoi(src, dst, thr, answer, n - 1)
    answer.append([src, dst])
    hanoi(thr, src, dst, answer, n - 1)
    return answer
def solution(n):
    return hanoi(1, 2, 3, [], n)
출처: https://alreadyusedadress.tistory.com/108?category=1188005 [ :티스토리]
