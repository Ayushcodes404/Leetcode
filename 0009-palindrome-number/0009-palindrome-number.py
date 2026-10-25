class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        rev = ""

        for i in range(-1, -len(s)-1, -1):
            rev = rev + s[i]

        if rev == s:
            return True
        else:
            return False