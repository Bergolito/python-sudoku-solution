


def _add(node, v):
    new = [v, [], []]
    if node:
        left, right = node[1:]
        if not left:
            left.extend(new)
        elif not right:
            right.extend(new)
        else:
            _add(left, v)
    else:
        node.extend(new)

def binary_tree(s):
    root = []
    for e in s:
        _add(root, e)
    return root

def traverse(n, order):
    if n:
        v = n[0]
        if order == 'pre':
            yield v
        for left in traverse(n[1], order):
            yield left
        if order == 'in':
            yield v
        for right in traverse(n[2], order):
            yield right
        if order == 'post':
            yield v
            
if __name__ == '__main__':
    tree = binary_tree('A B C D E F G'.split())
    print(tree)
    print('Niveis -> ',len(tree))
    print(list(traverse(tree, 'pre')))
    print(list(traverse(tree, 'in')))
    print(list(traverse(tree, 'post')))
    
    for (i,node) in enumerate(tree):
        print('[{}] => {}'.format(i,tree[i]))