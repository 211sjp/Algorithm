class RBTreeNode(object):
    def __init__(self, key, color='B'):
        self.key = key
        self.left = None
        self.right = None
        self.color = color
        self.p = None


class RBTree(object):
    def __init__(self):
        self.root = None


# 左旋算法
def LEFT_ROTATE(T, x):
    y = x.right
    x.right = y.left
    y.left.p = x
    y.p = x.p
    if x.p is None:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p =y


# 右旋算法
def RIGHT_ROTATE(T, x):
    y = x.left
    x.left = y.right
    y.right.p = x
    y.p = x.p
    if x.p is None:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y


def RBInsert(T, z):
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = None
    z.right = None
    z.color = 'R'
    RBInsertFixup(T, z)


def RBInsertFixup(T, z):
    while z.p and z.p.color == 'R':
        if z.p == z.p.p.left:              # case 1,2,3
            y = z.p.p.right
            if y.color == 'R':                  # case 1
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
    if z.left is None or z.right is None:         # case 1, 2
        y = z       # 后面进行物理删除y
    else:
        y = TreeSuccessor(z)        # y是z的中序后继
    if y.left is not None:
        x = y.left
    else:
        x = y.right
    x.p = y.p
    if y.p is None:        # y是根节点
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
    if x is not None:
        MidOrder(x.left)
        print('key:', x.key, 'x.parent:', x.p.key if x.p else 'None')
        MidOrder(x.right)
    

def TreeSuccessor(x):
    if x.right is None:
        q = x.p
        while q is not None and x == q.right:
            x = q
            q = q.p
    else:
        q = x.right
        p = q
        while p.left is not None:
            q = p
            p = p.left
    return q


def main():
    nodes = [11, 2, 14, 1, 7, 15, 5, 8, 4]
    T = RBTree()
    for node in nodes:
        RBInsert(T, RBTreeNode(node))
        print("插入数据", node)
    print('中序遍历')
    MidOrder(T.root)


if __name__ == '__main__':
    main()
