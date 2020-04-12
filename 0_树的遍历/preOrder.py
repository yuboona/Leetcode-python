def preorder(root):
    """迭代式 前序遍历
    """
    stack = []
    stack.append(root)
    while len(stack) != 0:
        cur = stack.pop()       # 从栈尾弹出
        print(cur.val)      # 前序访问
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    