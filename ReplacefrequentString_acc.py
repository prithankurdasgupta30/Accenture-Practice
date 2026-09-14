def replaceString(s, c):
    mp = {}
    for ch in s:
        if ch in mp:
            mp[ch] += 1
        else:
            mp[ch] = 1
    max_count = 0
    max_char = ''
    for ch, count in mp.items():
        if count > max_count:
            max_count = count
            max_char = ch
    return s.replace(max_char, c)

s = input()
print(replaceString(s,'t'))