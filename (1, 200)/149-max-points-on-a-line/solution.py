from itertools import permutations

class Solution(object):
    def maxPoints(self, points):
        def getLine(a, b, max_y_or_x, min_y_or_x):
            if a[0] == b[0]:
                return [[a[0], y] for y in range(min_y_or_x, max_y_or_x + 1)]
            if a[1] == b[1]:
                return [[x, a[1]] for x in range(min_y_or_x, max_y_or_x + 1)]
            m = (b[1] - a[1]) / (b[0] - a[0])
            b = a[1] - m * a[0]
            return [[x, round(m * x + b)] for x in range(min_y_or_x, max_y_or_x + 1)]

        def getPointsOnLine(line, points):
            count = 0
            for point in points:
                if point in line:
                    count += 1
            return count

        max_y_or_x = 0
        min_y_or_x = 0
        for point in points:
            if point[0] > max_y_or_x:
                max_y_or_x = point[0]
            if point[0] < min_y_or_x:
                min_y_or_x = point[0]
            if point[1] > max_y_or_x:
                max_y_or_x = point[1]
            if point[1] < min_y_or_x:
                min_y_or_x = point[1]

        max_points = 1
        for a, b in permutations(points, 2):
            line = getLine(a, b, max_y_or_x, min_y_or_x)
            points_on_line = getPointsOnLine(line, points)
            if points_on_line > max_points:
                max_points = points_on_line

        return max_points

def test(s):
    assert s.maxPoints([[1,1],[2,2],[3,3]]) == 3
    assert s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) == 4
    assert s.maxPoints([[2,3],[3,3],[-5,3]]) == 3
    assert s.maxPoints([[3,10],[0,2]]) == 2
    assert s.maxPoints([[0,2],[3,10]]) == 2
    assert s.maxPoints([[-6,-1],[3,1],[12,3]]) == 3
    assert s.maxPoints([[84,250],[0,0],[0,-70],[-42,-230],[21,10],[42,90],[1,0],[1,-1]]) == 5

test(s = Solution())

class Solution2(object):
    def maxPoints(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def maxPointsOnLine(i, points):
            slopes = {}
            max_points = 0
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0:
                    slope = (0, 1)
                elif dy == 0:
                    slope = (1, 0)
                else:
                    g = gcd(dx, dy)
                    slope = (dx / g, dy / g)
                if slope in slopes:
                    slopes[slope] += 1
                else:
                    slopes[slope] = 1
                max_points = max(max_points, slopes[slope])
            return max_points + 1

        max_points = 0
        for i in range(len(points)):
            max_points = max(max_points, maxPointsOnLine(i, points))
        return max_points

test(s = Solution2())
