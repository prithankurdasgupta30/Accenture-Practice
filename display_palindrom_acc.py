def isPalindrome(num):
        return str(num) == str(num)[::-1]
def displayPalindrome(lower, upper):
        res = []
        for num in range(lower+1, upper):
                if isPalindrome(num):
                        res.append(num)
        return res
lower = int(input())
upper = int(input())
print(displayPalindrome(lower, upper))