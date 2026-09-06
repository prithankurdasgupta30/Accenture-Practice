def replaceChar(n, ch1, ch2):
        result = ""
        if n != None:
                result = n.replace(ch1,'*').replace(ch2,ch1).replace('*',ch2)
                return result
        return 'Null' 
n = input()
ch1, ch2 = map(str, input().split())
print(replaceChar(n, ch1, ch2))