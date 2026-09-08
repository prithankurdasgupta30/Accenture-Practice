def firstKWords(s,k):
        words = s.split()
        return ' '.join(words[:k])
s = input()
k = int(input())
print(firstKWords(s,k))