class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    if len(self.storage) == 1: return self.storage.pop()
    ret = self.storage[0]
    # move last to first then remove last
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return ret

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 0: return

    parent_index = int((index - 1) / 2) # can never be < 0 because truncate unless index is < 0
    child_value = self.storage[index]
    parent_value = self.storage[parent_index]

    if child_value > parent_value:
      # swap
      self.storage[index] = parent_value
      self.storage[parent_index] = child_value

      self._bubble_up(parent_index)

    # TODO iterative vs recursive speed

  def _sift_down(self, index):
    first_child_index = int(index * 2) + 1

    parent_value = self.storage[index]

    max_child_index = index
    max_child_value = self.storage[max_child_index]

    # find the max value between parent and children
    for n in range(2):
      child_index = first_child_index + n
      if child_index < len(self.storage):
        child_value = self.storage[child_index]
        if child_value > max_child_value:
          max_child_index = child_index
          max_child_value = child_value

    if max_child_index != index: # not parent
      # swap parent to child
      self.storage[max_child_index] = parent_value
      self.storage[index] = max_child_value
      self._sift_down(max_child_index)

h = Heap()
h.insert(6)
h.insert(7)
h.insert(5)
h.insert(8)
h.insert(10)
h.insert(1)
h.insert(2)
h.insert(5)
print(h.storage)