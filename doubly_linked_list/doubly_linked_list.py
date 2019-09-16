"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length
  
  """Wraps the given value in a ListNode and inserts it 
  as the new head of the list. Don't forget to handle 
  the old head node's previous pointer accordingly."""
  def add_to_head(self, value):
    node = ListNode(value)
    return self.add_node_to_head(node)

  def add_node_to_head(self, node):
    if self.length == 0:
        self.head = node
        self.tail = node # add as tail too
    else:
      self.head.prev = node
      node.next = self.head
      node.prev = None
      self.head = node

    self.length += 1
    return node
  
  """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""
  def remove_from_head(self):
    if self.length == 0: return

    old_head = self.head
    self.head = self.head.next
    if self.head != None:
      self.head.prev = None
    if self.tail == old_head: # remove tail too
      self.tail = None

    self.length -= 1

    old_head.next = None
    old_head.prev = None
    return old_head.value

  """Wraps the given value in a ListNode and inserts it 
  as the new tail of the list. Don't forget to handle 
  the old tail node's next pointer accordingly."""
  def add_to_tail(self, value):
    node = ListNode(value)
    return self.add_node_to_tail(node)

  def add_node_to_tail(self, node):
    if self.length == 0:
      self.tail = node
      self.head = node # add as head too
    else:
      self.tail.next = node
      node.prev = self.tail
      node.next = None
      self.tail = node

    self.length += 1
    return node

  """Removes the List's current tail node, making the 
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""
  def remove_from_tail(self):
    if self.length == 0: return

    old_tail = self.tail
    self.tail = self.tail.prev
    if self.tail != None:
      self.tail.next = None
    if self.head == old_tail: # remove head too
      self.head = None

    self.length -= 1

    old_tail.next = None
    old_tail.prev = None
    return old_tail.value

  """Removes the input node from its current spot in the 
  List and inserts it as the new head node of the List."""
  def move_to_front(self, node):
    if self.length < 2: return

    self.delete(node)
    self.add_node_to_head(node)      

  """Removes the input node from its current spot in the 
  List and inserts it as the new tail node of the List."""
  def move_to_end(self, node):
    if self.length < 2: return

    self.delete(node)
    self.add_node_to_tail(node)

  """Removes a node from the list and handles cases where
  the node was the head or the tail"""
  def delete(self, node):
    # TODO does this assume the node is part of the link
    # assumes node is part of link
    if node == self.head:
      self.head = self.head.next
      if self.head != None:
        self.head.prev = None

      if node == self.tail: # also the tail
        self.tail = self.tail.prev
        if self.tail != None:
          self.tail.next = None
    elif node == self.tail:
      self.tail = self.tail.prev
      if self.tail != None:
        self.tail.next = None

      if node == self.head: # also the head
        self.head = self.head.next
        if self.head != None:
          self.head.prev = None
    else:
      node.next.prev = node.prev
      node.prev.next = node.next

    node.prev = None
    node.next = None

    self.length -= 1
    
  """Returns the highest value currently in the list"""
  def get_max(self):
    if self.head == None: return None

    max = self.head.value

    node = self.head.next
    while node != None:
      if node.value > max:
        max = node.value

      node = node.next

    return max

  def __str__(self):
    if self.length == 0: return ""

    dllstr = ""
    node = self.head
    while True:
      dllstr += str(node.value)
      node = node.next
      if node != None:
        dllstr += ","
      else:
        break

    return dllstr

# node1 = ListNode(1)
# dll = DoublyLinkedList(node1)
# print(dll)

# node2 = dll.add_to_head(2)
# print(dll)

# node3 = dll.add_to_tail(3)
# print(dll)

# dll.delete(node1)
# print(dll)

# node1b = dll.add_to_head(1)
# print(dll)

# dll.delete(node3)
# print(dll)

# dll.delete(node2)
# print(dll)

# dll.delete(node1b)
# print(dll)