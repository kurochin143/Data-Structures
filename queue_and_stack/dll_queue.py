import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.dll = DoublyLinkedList()

  def enqueue(self, item):
    self.dll.add_to_tail(item)
  
  def dequeue(self):
    return self.dll.remove_from_head()

  def len(self):
    return len(self.dll)
