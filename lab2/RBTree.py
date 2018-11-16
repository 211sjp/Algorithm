class RBTreeNode(object):
    def __init__(self, key, color = 'R'):
        self.key = key
        self.left = None
        self.right = None
        self.color = color
        self.p = None

    def is_black_node(self):
        return self.color == 'B'

    def set_black_node(self):
        self.color = 'B'

    def set_red_node(self):
        self.color = 'R'

    def get_key(self):
        return self.key 


class RBTree(object):
    def __init__(self):
        self.root = None


# 左旋算法
def LEFT_ROTATE(RBTree T, RBTreeNode x ):
    y = x.right
    x.right = y.left
    y.left.p = x
    y.p = x.p
    if x.p == None:
        T.root = y
    elif x = x.p.left
        x.p.left = y
    else x.p.right = y
    y.left = x
    x.p =y

# 右旋算法
def RIGHT_ROTATE(RBTree T, RBTreeNode x ):
    y = x.left
    x.left = y.right
    y.right.p = x
    y.p = x.p
    if x.p == None:
        T.root = y
    elif x = x.p.right
        x.p.right = y
    else x.p.left = y
    y.right = x
    x.p =y