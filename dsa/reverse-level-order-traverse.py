import copy

def main():
  root = make_tree()

  cur, nex, result = [], [], []
  cur.append(root)
  
  while cur or nex:
   cur, nex, out = update_cur_nex(cur, nex)
   result.append(out)

#    print([x for x in result])
#    print([x.val for x in cur])
#    print([x.val for x in nex])

  result.reverse()
  print(result)

def make_tree():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  return root

# to unittest
def update_cur_nex(cur, nex):
  out = []
  while cur:
    tmp = cur.pop(0)
    out.append(tmp.val)
    if tmp.left:
      nex.append(tmp.left)
    if tmp.right:
      nex.append(tmp.right)
  cur = nex
  nex = []
  return cur, nex, out

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

if __name__ == '__main__':
    main()  