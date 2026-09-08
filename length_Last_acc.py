def lengthLastWord(s):
        arr = []
        words = s.split()
        for word in words:
                arr.append(len(word))
        return arr[-1] if arr else 0
s = input()
print(lengthLastWord(s))