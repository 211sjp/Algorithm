import turtle
t = turtle.Turtle()
NIL = -10000

"""
区间树的数据结构
"""


class interval(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high


class INTTreeNode(object):
    def __init__(self, int, color='B'):
        self.int = int
        self.key = int.low
        self.left = None
        self.right = None
        self.color = color
        self.p = None
        self.max = int.high

    def set_max(self):
        self.max = max(self.int.high, self.left.max, self.right.max)


class INTTree(object):
    def __init__(self):
        self.nil = INTTreeNode(interval(NIL, NIL+1))
        self.root = self.nil


"""
区间树的基本操作
"""


# 左旋算法
def LEFT_ROTATE(T, x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y
    # 区间树设置max
    x.set_max()
    y.set_max()


# 右旋算法
def RIGHT_ROTATE(T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y
    # 区间树设置max
    x.set_max()
    y.set_max()


def INTInsert(T, z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = 'R'
    INTInsertFixup(T, z)


def INTInsertFixup(T, z):
    while z.p and z.p.color == 'R':
        if z.p == z.p.p.left:              # case 1,2,3
            y = z.p.p.right
            if y and y.color == 'R':                  # case 1
                y.color = 'B'
                z.p.color = 'B'
                z.p.p.color = 'R'
                z = z.p.p
            else:                              
                if z == z.p.right:              # case 2
                    z = z.p
                    LEFT_ROTATE(T, z)
                z.p.color = 'B'                 # case 3
                z.p.p.color = 'R'
                RIGHT_ROTATE(T, z.p.p)
        else:                                           # case 4,5,6
            y = z.p.p.left
            if y.color == 'R':                  # case 4
                y.color = 'B'
                z.p.color = 'B'
                z.p.p.color = 'R'
                z = z.p.p
            else:
                if z == z.p.left:               # case 5
                    z = z.p
                    RIGHT_ROTATE(T, z)
                z.p.color = 'B'                 # case 6
                z.p.p.color = 'R'
                LEFT_ROTATE(T, z.p.p)
    T.root.color = 'B'


def INTDelete(T, z):
    if z.left == T.nil or z.right == T.nil:         # case 1, 2
        y = z       # 后面进行物理删除y
    else:
        y = TreeSuccessor(T, z)        # y是z的中序后继
    if y.left != T.nil:
        x = y.left
    else:
        x = y.right
    if x:
        x.p = y.p
    if y.p == T.nil:        # y是根节点
        T.root = x
    else:                           # y非根
        if y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
    if y != z:             # case 3
        z.key = y.key
        z.color = y.color
    if y.color == 'B':
        INTDeleteFixup(T, x)
    return y


def INTDeleteFixup(T, x):
    while x != T.root and x.color == 'B':
        if x == x.p.left:
            w = x.p.right
            if w.color == 'R':
                w.color = 'B'
                x.p.color = 'R'
                LEFT_ROTATE(T, x.p)
                w = x.p.right
            if w.left.color == 'B' and w.right.color == 'B':
                w.color = 'R'
                x = x.p
            else:
                if w.right.color == 'B':
                    w.left.color = 'B'
                    w.color = 'R'
                    RIGHT_ROTATE(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = 'B'
                w.right.color ='B'
                LEFT_ROTATE(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == 'R':
                w.color = 'B'
                x.p.color = 'R'
                RIGHT_ROTATE(T, x.p)
                w = x.p.left
            if w.right.color == 'B' and w.left.color == 'B':
                w.color = 'R'
                x = x.p
            else:
                if w.left.color == 'B':
                    w.right.color = 'B'
                    w.color = 'R'
                    LEFT_ROTATE(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = 'B'
                w.left.color ='B'
                RIGHT_ROTATE(T, x.p)
                x = T.root
    x.color = 'B'


def INTSearch(T, i):
    x = T.root
    while x != T.nil and i.low >= x.int.high or i.high <= x.int.low:
        if x.left != T.nil and x.left.max >= i.low:
            x = x.left
        else:
            x = x.right
    return x


"""
辅助函数
"""


def MidOrder(x):
    if x.key != NIL:
        MidOrder(x.left)
        print('key:', x.key, 'x.parent:', x.p.key if x.p.key != NIL else 'nil')
        MidOrder(x.right)


def Locate(root, key):
    if root.key == NIL:
        return None
    if key == root.key:
        return root
    p = Locate(root.left, key)
    if p:
        return p
    else:
        return Locate(root.right, key)


def TreeSuccessor(T, x):
    if not x.right or x.right == T.nil:
        q = x.p
        while q and q != T.nil and x == q.right:
            x = q
            q = q.p
    else:
        q = x.right
        p = q
        while p.left and p.left != T.nil:
            q = p
            p = p.left
    return q


"""
turtle画图
"""


def height(root):
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))


def jump_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw(node, x, y, dx):
    if node:
        t.goto(x, y)
        jump_to(x, y - 20)
        t.begin_fill()
        t.fillcolor('red' if node.color == 'R' else 'black')
        t.circle(25)
        t.end_fill()
        t.color('green')
        t.write("[{},{}]/{}".format(node.int.low, node.int.high, node.max) if node.key != NIL else 'nil', font=("Arial", 15), align="center")
        t.color('red' if node.color == 'R' else 'black')
        draw(node.left, x - dx, y - 60, dx / 2)
        jump_to(x, y - 20)
        draw(node.right, x + dx, y - 60, dx / 2)


"""
主函数
"""


def main():
    nodes = [interval(5, 8), interval(15, 22), interval(16, 25), interval(13, 21), interval(29, 61)]
    T = INTTree()
    for node in nodes:
        print("插入数据", node)
        INTInsert(T, INTTreeNode(node))
        print("颜色：", Locate(T.root, node.low).color)
    print('中序遍历')
    MidOrder(T.root)
    # INTDelete(T, T.root)
    # INTDelete(T, Locate(T.root, 13))
    result = INTSearch(T, interval(3, 9))
    if result != T.nil:
        print("找到的区间为：[", result.int.low, ",", result.int.high, ']')
    else:
        print("没有重叠区间！")


    # 画图
    t.speed(0)
    h = height(T.root)
    jump_to(0, 30 * h)
    draw(T.root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
