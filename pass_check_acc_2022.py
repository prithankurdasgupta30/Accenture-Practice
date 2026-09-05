def checkPassword(s,n):
        if len(s) < 4:
                return 0
        if s[0].isdigit():
                return 0
        cap = 0
        n = 0
        for i in range(len(s)):
                if s[i] == " " or s[i] == "/":
                        return 0
                if s[i] >= "A" and s[i] <= "Z":
                        cap += 1
                if s[i].isdigit():
                        n += 1
        if cap >=1 and n >= 1:
                return 1
        else:
                return 0
s = input()
n = len(s)
print(checkPassword(s,n))