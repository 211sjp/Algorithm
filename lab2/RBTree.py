import turtle
t = turtle.Turtle()
NIL = -10000


"""
红黑树的数据结构
"""


class RBTreeNode(object):
    def __init__(self, key, color='B'):
        self.key = key
        self.left = None
        self.right = None
        self.color = color
        self.p = None


class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(NIL)
        self.root = self.nil

T = RBTree()


"""
红黑树的基本操作
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


def RBInsert(T, z):
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
    RBInsertFixup(T, z)


def RBInsertFixup(T, z):
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


def RBDelete(T, z):
    y = z
    y_original_color = y.color
    if z.left == T.nil:
        x = z.right
        RBTransplant(T, z, z.right)
    elif z.right == T.nil:
        x = z.left
        RBTransplant(T, z, z.left)
    else:
        y = TreeMinimum(z.right)
        y_original_color = y.color
        x = y.right
        if y.p == z:
            x.p = y
        else:
            RBTransplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        RBTransplant(T, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    if y_original_color == 'B':
        RBDeleteFixup(T, x)


def RBDeleteFixup(T, x):
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
                w.right.color = 'B'
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
                w.left.color = 'B'
                RIGHT_ROTATE(T, x.p)
                x = T.root
    x.color = 'B'


"""
辅助函数
"""


def MidOrder(x):
    if x.key != NIL:
        MidOrder(x.left)
        print('key:', x.key, 'x.p:', x.p.key if x.p.key!=NIL else 'nil')
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


def RBTransplant( T, u, v):
    if u.p == T.nil:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p


def TreeMinimum(x):
    while x.left != T.nil:
        x = x.left
    return x


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
        t.color('white')
        t.write(node.key if node.key != NIL else 'nil', font=("Arial",25), align="center")
        t.color('red' if node.color == 'R' else 'black')
        t.end_fill()
        draw(node.left, x - dx, y - 60, dx / 2)
        jump_to(x, y - 20)
        draw(node.right, x + dx, y - 60, dx / 2)


"""
主函数
"""


def main():
    nodes = [1, 6, 11, 8, 13, 25, 17, 15, 22, 67]
    for node in nodes:
        print("插入数据", node)
        RBInsert(T, RBTreeNode(node))
        print("颜色：",Locate(T.root, node).color)
    print('中序遍历')
    MidOrder(T.root)
    RBDelete(T, T.root)
    # RBDelete(T, Locate(T.root, 6))

    # 画图
    t.speed(0)
    h = height(T.root)
    jump_to(0, 30 * h)
    draw(T.root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
