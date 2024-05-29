class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        shots = 1
        curr = points[0][1]
        for point in points:
            if point[0] > curr:
                curr = point[1]
                shots = shots + 1
            else:
                curr = min(curr, point[1])
        return shots