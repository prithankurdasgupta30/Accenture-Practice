def mostFreqVow(str):
        freqVow = {}
        maxVow = 0
        mostFreqVow = None
        for ch in str:
                if ch in 'aeiou':
                        freqVow[ch] = freqVow.get(ch,0)+1
                        if freqVow[ch] > maxVow:
                                maxVow = freqVow[ch]
                                mostFreqVow = ch
        return mostFreqVow
s = input()
print(mostFreqVow(s))