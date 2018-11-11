import math


class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


def dis(p,q):
    xtmp = (p.x - q.x)*(p.x - q.x)
    ytmp = (p.y - q.y)*(p.y - q.y)
    return math.sqrt(xtmp + ytmp)


def cmp(p,q):
    if p.x != q.x:
        return p.x - q.x
    else:
        return p.y - q.y


INF = 100000000
PointArray = []


def NearestPair(left, right):
    d = INF
    if (left == right):
        return -INF,-INF,d
    if (left + 1 == right):
        return left,right,dis(PointArray[left],PointArray[right])
    mid = int((left + right)/2)
    p1l,p2l,dl = NearestPair(left, mid)
    p1r,p2r,dr = NearestPair(mid+1, right)
    d = min(dl,dr)
    #print("d:",d)
    if d==dl:
        p1=p1l
        p2=p2l
    else:
        p1=p1r
        p2=p2r
    SeamArray = []
    for i in range(left, right+1):
        if abs(PointArray[mid].x-PointArray[i].x <= d):
            SeamArray.append(i)
    SeamArray.sort(key = lambda p : PointArray[p].y)
    for i in range(len(SeamArray)):
        for j in range(i+1, len(SeamArray)):
            if PointArray[SeamArray[j]].y - PointArray[SeamArray[i]].y < d:
                distance = dis(PointArray[SeamArray[j]],PointArray[SeamArray[i]])
                if distance < d:
                    p1 = SeamArray[j]
                    p2 = SeamArray[i]
                    d = distance
                    # print("distance",distance)
    return p1, p2, d


def ReadData(testfile):
    with open(testfile, 'r') as f1:
        test1 = f1.read()
        l1 = test1.split(';')
        n = len(l1)
        parray = []
        for i in l1:
            point = i.split(',')
            parray.append(Point(point[0],point[1]))
    return n, parray            

for  i in range(1,4):
    n,PointArray = ReadData('test%d.txt' %i)
    '''
    暴力法
    minn = 10000
    for  j  in range(n):
        for k in range(j+1,n):
            dist = dis(Point(PointArray[j].x,PointArray[j].y),Point(PointArray[k].x,PointArray[k].y))
            if dist < minn:
                minn = dist
    print(minn)
    '''

    PointArray.sort(key=lambda p:p.x)
    p1,p2,d=NearestPair(0,n-1)
    print("{}文件测试的结果：最近点对为:({},{})({},{})最近点对距离：{}".format('test%d.txt' %i,PointArray[p1].x,PointArray[p1].y,PointArray[p2].x,PointArray[p2].y,d))
