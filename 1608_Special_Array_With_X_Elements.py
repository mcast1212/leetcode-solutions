class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sol = 0
        for x in range(len(nums)+1):
            for i in range(len(nums)):
                print('x: ',x,'i: ',i,'sol: ',sol)
                if nums[i] >= x:
                    sol = sol + 1
            if x == sol:
                return x
            else:
                sol = 0
        return -1