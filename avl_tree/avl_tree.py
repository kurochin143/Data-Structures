"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
  def __init__(self, node=None):
    self.node = node
    # init height to -1 because of 0-indexing
    self.height = -1
    self.balance = 0

  """
  Display the whole tree. Uses recursive def.
  """
  def display(self, level=0, pref=''):
    self.update_height()  # Update height before balancing
    self.update_balance()
    
    if self.node != None: 
      print ('-' * level * 2, pref, self.node.key,
        f'[{self.height}:{self.balance}]',
        'L' if self.height == 0 else ' ')
      if self.node.left != None:
        self.node.left.display(level + 1, '<')
      if self.node.right != None:
        self.node.right.display(level + 1, '>')

  """
  Computes the maximum number of levels there are
  in the tree
  """
  def update_height(self):
    if self.node.left != None:
      left_height = self.node.left.height
    else:
      left_height = 0
    if self.node.right != None:
      right_height = self.node.right.height
    else:
      right_height = 0

    self.height = 1 + max(left_height, right_height)

  """
  Updates the balance factor on the AVLTree class
  """
  def update_balance(self):
    if self.node.left == None and self.node.right == None:
      self.balance = 0
      return

    if self.node.left != None:
      left_height = self.node.left.height
    else:
      left_height = 0
    if self.node.right != None:
      right_height = self.node.right.height
    else:
      right_height = 0

    self.balance = right_height - left_height

  """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """
  def left_rotate(self):
    old_self_node = self.node
    old_right_avl = self.node.right
    self.node = self.node.right.node
    old_right_avl.node = old_self_node
    old_self_node.right = self.node.left
    self.node.left = old_right_avl

    self.node.left.update_height()
    self.node.left.update_balance()

    self.update_height()
    self.update_balance()

  """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """
  def right_rotate(self):
    old_self_node = self.node
    old_left_avl = self.node.left
    self.node = self.node.left.node
    old_left_avl.node = old_self_node
    old_self_node.left = self.node.right
    self.node.right = old_left_avl

    self.node.right.update_height()
    self.node.right.update_balance()

    self.update_height()
    self.update_balance()

  """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """
  def rebalance(self):
    if self.balance < -1:
      if self.node.left.balance > 0: # left right
        self.node.left.left_rotate()
        self.right_rotate()
      else: # left left
        self.right_rotate()
    elif self.balance > 1:
      if self.node.right.balance < 0: # right left
        self.node.right.right_rotate()
        self.left_rotate()
      else: # right right
        self.left_rotate()


  """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """
  def insert(self, key):
    if self.node == None:
      self.node = Node(key)
      self.height = 1
      return

    if key < self.node.key:
      if self.node.left != None:
        self.node.left.insert(key)
      else:
        self.node.left = AVLTree(Node(key))
        self.node.left.height = 1
    else:
      if self.node.right != None:
        self.node.right.insert(key)
      else:
        self.node.right = AVLTree(Node(key))
        self.node.right.height = 1

    self.update_height()
    self.update_balance()
    self.rebalance()

root = AVLTree(Node(5))
root.insert(3)
root.insert(6)
root.insert(5)
root.insert(7)
root.insert(8)
root.display()