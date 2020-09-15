def solution(S):
    for i in range (1, len(S)+1):
        a ={}
        for j in range(len(S)-i+1):
            try:
                a[S[j:j+i]] += 1
            except:
                a[S[j:j+i]] = 1
        
        uni = False
        for key in a:
            if a[key] == 1:
                uni = True
        
        if uni:  
            return i

print(solution("abaaba"))
print(solution("zyzyzyz"))
print(solution("aabbbabaaa"))