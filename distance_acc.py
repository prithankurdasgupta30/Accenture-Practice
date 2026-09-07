import math
def dist(x1,y1,x2,y2,x3,y3):
        d1 = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
        d2 = math.sqrt(math.pow((x3-x2),2) + math.pow((y3-y2),2))
        d3 = math.sqrt(math.pow((x1-x3),2) + math.pow((y1-y3),2))
        nd1 = round(d1,2)
        nd2 = round(d2,2)
        nd3 = round(d3,2)
        return nd1,nd2,nd3
x1,y1,x2,y2,x3,y3 = map(int, input().split())
print(dist(x1,y1,x2,y2,x3,y3))