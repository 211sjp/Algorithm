import turtle
t = turtle.Turtle()


class RBTreeNode(object):
    def __init__(self, key, color='B'):
        self.key = key
        self.left = None
        self.right = None
        self.color = color
        self.p = None


class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil


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
    if x.p== T.nil:
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
        RBDeleteFixup(T, x)
    return y


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


def MidOrder(x):
    if x.key != 0:
        MidOrder(x.left)
        print('key:', x.key, 'x.parent:', x.p.key if x.p.key!=0 else 'nil')
        MidOrder(x.right)


def Locate(root, key):
    if root.key == 0:
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
        t.write(node.key if node.key != 0 else 'nil', font=("Arial",25), align="center")
        t.color('red' if node.color == 'R' else 'black')
        t.end_fill()
        draw(node.left, x - dx, y - 60, dx / 2)
        jump_to(x, y - 20)
        draw(node.right, x + dx, y - 60, dx / 2)


def main():
    nodes = [5, 6, 15, 22, 45, 25, 21, 13, 29, 61]
    T = RBTree()
    for node in nodes:
        print("插入数据", node)
        RBInsert(T, RBTreeNode(node))
        print("颜色：",Locate(T.root, node).color)
    print('中序遍历')
    MidOrder(T.root)
    # RBDelete(T, T.root)
    # RBDelete(T, Locate(T.root, 13))

    # 画图
    t.speed(0)
    h = height(T.root)
    jump_to(0, 30 * h)
    draw(T.root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.done()


if __name__ == '__main__':
    main()
