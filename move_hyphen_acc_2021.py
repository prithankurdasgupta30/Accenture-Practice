def movehyphentofront(s):
        c = 0
        final = ""
        for i in s:
                if i == '-':
                        c += 1
                else:
                        final += i
        return ('-'*c + final)
s = input()
print(movehyphentofront(s))