import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.dll = DoublyLinkedList()

  def push(self, value):
    self.dll.add_to_tail(value)
  
  def pop(self):
    self.dll.remove_from_tail()

  def len(self):
    return len(self.dll)
