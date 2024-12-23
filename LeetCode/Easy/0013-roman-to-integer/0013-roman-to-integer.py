class Solution(object):
    def romanToInt(self, s):

        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0

        for i in range(0,len(s)-1):
            if dic[s[i]]>=dic[s[i+1]]:
                sum = sum+dic[s[i]]
            else :
                sum = sum-dic[s[i]]
        return sum+dic[s[-1]]