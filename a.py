def a(strs):
    if not strs:
        return ''
    s1 = min(strs) #flight
    s2 = max(strs) #flower
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1

print(a(["flower","flow","flight"]))