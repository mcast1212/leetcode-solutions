class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        num = int(s, 2)
        while num != 1:
            if num%2==0:
                num = num/2
            else:
                num = num + 1
            count = count + 1
        return count
