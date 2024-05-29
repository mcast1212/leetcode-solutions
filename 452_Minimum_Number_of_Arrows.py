class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        shots = 1
        curr = points[0][1]
        extra = []
        for point in points:
            if point[0] > curr:
                curr = point[1]
                shots = shots + 1
            elif point[0] < curr and point[1] < curr:
                extra.append(point)
        if not extra:
            return shots
        shots = shots + 1
        curr = extra[0][1]
        for point in extra:
            if point[0] > curr:
                curr = point[1]
                shots = shots + 1
        return shots