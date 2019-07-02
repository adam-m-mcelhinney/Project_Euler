# Triangle containment
#
# Problem 102
# Three distinct points are plotted at random on a Cartesian plane,
# for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.
#
# Consider the following two triangles:
#
# A(-340,495), B(-153,-910), C(835,-947)
#
# X(-175,41), Y(-421,-714), Z(574,-645)
#
# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
#
# Using triangles.txt (right click and 'Save Link/Target As...'),
# a 27K text file containing the co-ordinates of one thousand "random" triangles,
# find the number of triangles for which the interior contains the origin.
#
# NOTE: The first two examples in the file represent the triangles in the example given above.

'''Notes:
1. I believe this is a point in polygon problem. If I can find a straightforward
point in polygon algorithm, maybe that will just solve it.
2. If all of the points are above zero or below zero, then doesnt contain origin.

--> Looks like there is a lot of ways of doing this, particularly for triangles.
This area method is super easy to understand, but probably not super efficient.
Basically, make triangles out of your test point and triangel vertices. If the
total of those areas equals the total of the whole triangle, then the point is
in the triangle.
https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/
'''


filePath = '/Users/amcelhinney/repos/Project_Euler/p102_triangles.txt'

with open(filePath) as f:
    content = f.readlines()

inputStr = '-340,495,-153,-910,835,-947\n'
def formatPoints(inputStr):
    t = inputStr.replace('\n', '').split(',')
    points = [(int(t[i]), int(t[i+1])) for i in range(0, len(t), 2)]
    return points

allTriangles = []
for i in content:
    allTriangles.append(formatPoints(i))


def areaOfTriangle(p1, p2, p3):
    '''https://www.mathopenref.com/coordtrianglearea.html'''
    area = abs(p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1]))/2
    return area

testPoint = [(15, 15), (23, 30), (50, 25)]

assert(areaOfTriangle(testPoint[0], testPoint[1], testPoint[2]) == 222.5)

# Note: since this is in the origin, I could simplify this area formula for that case
def inTriangle(trianglePoints):
    p1 = trianglePoints[0]
    p2 = trianglePoints[1]
    p3 = trianglePoints[2]
    origin = (0, 0)
    totalArea = areaOfTriangle(p1, p2, p3)
    a1 = areaOfTriangle(p1, p2, origin)
    a2 = areaOfTriangle(p1, p3, origin)
    a3 = areaOfTriangle(p2, p3, origin)
    if totalArea == a1 + a2 + a3:
        return 1
    else:
        return 0


i = 0
for triangle in allTriangles:
    i += inTriangle(triangle)




