s = input()
s = list(s)
for i in range(len(s)):
    if (s[i] >= 'a') & (s[i] <= 'z'):
        s[i] = chr(ord(s[i]) + ord('A') - ord('a'))
    elif (s[i] >= 'A') & (s[i] <= 'Z'):
        s[i] = chr(ord(s[i]) - ord('A') + ord('a'))
print(''.join(s))