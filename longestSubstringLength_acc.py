def lengthLongestSubstring(s):
        seen = set()
        left = 0
        max_Length = 0
        for right in range(len(s)):
                while s[right] in seen:
                        seen.remove(s[left])
                        left+=1
                seen.add(s[right])
                max_Length = max(max_Length, right-left+1)
        return max_Length
s = input()
print(lengthLongestSubstring(s))