# Write a function solution that, given a string S of length N, 
# returns the length of the shortest unique substring of S, that is, the length of the shortest word which occurs in S exactly once. 
# Examples: 
# 1. Given S = "abaaba", the function should return 2. The shortest unique substring of S is "aa". 
# 2. Given S = "zyzyzyz", the function should return 5. The shortest unique substring of S is "yzyzy". 
# Note that there are shorter words, like "yzy", occurrences of which overlap, but they still count as multiple occurrences. 
# 3. Given S = "aabbbabaaa", the function should return 3. All substrings of size 2 occurs in S at least twice. 
# Assume that: N is an integer within the range [1..200]; • string S consists only of lowercase letters (a-z). 
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment. 

def solution(S):
    for i in range (1, len(S)+1):
        a ={}
        for j in range(len(S)-i+1):
            try:
                a[S[j:j+i]] += 1
            except:
                a[S[j:j+i]] = 1

        print(i,j)
        print(a)

        uni = False
        for key in a:
            if a[key] == 1:
                uni = True
        
        if uni:  
            return i

print(solution("abaaba")) #2
#print(solution("zyzyzyz")) #5
#print(solution("aabbbabaaa")) #3