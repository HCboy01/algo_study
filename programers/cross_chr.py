def cross_chr(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    ans = list(range(len(s1) + len(s2)))

    for i in (range(len(s1) + len(s2))):
        if i % 2 == 0:
            ans[i] = s1[i // 2]
        else:
            ans[i] = s2[i // 2]
    return ("".join(ans))