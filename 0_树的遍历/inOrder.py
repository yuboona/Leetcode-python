def inOrder(root):
    """迭代式 中序遍历
        - 中序讲究遍历到左节点的最深处才开始访问
        - 使用cur指针来指向每一个节点进行压栈，因为压栈不是靠弹出栈顶的
    Parameters
    ----------
    root : node
        根节点
    """

    stack = []
    stack.append(root)
    cur = root
    while len(stack) != 0:
        while cur.left is not None:
            stack.append(cur.left)
            cur = cur.left
        out = stack.pop()
        print(out.val)      # 中序输出

        if out.right is not None:
            # 关于当前节点的右子节点，两种情况：有或无
            stack.append(out.right)
            cur = out.right
        else:
            stack[-1].left = None        # 这样保证了父节点不再压栈左节点
            cur = stack[-1]
