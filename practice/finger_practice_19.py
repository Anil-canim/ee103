# In this problem, you will implement two classes according to the specification below: one Container class and
# one Stack class (a subclass of Container).
# Our Container class will initialize an empty list. The two methods we will have are to calculate the size of the
# list and to add an element. The second method will be inherited by the subclass. We now want to create a
# subclass so that we can add more functionality -- the ability to remove elements from the list. A Stack will add
# elements to the list in the same way, but will behave differently when removing an element.
# A stack is a last in, first out data structure. Think of a stack of pancakes. As you make pancakes, you create a
# stack of them with older pancakes going on the bottom and newer pancakes on the top. As you start eating the
# pancakes, you pick one off the top so you are removing the newest pancake added to the stack. When
# implementing your Stack class, you will have to think about which end of your list contains the element that
# has been in the list the shortest amount of time. This is the element you will want to remove and return.
class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []
    def size(self):
        """
        Returns the length of the container list
    """
        return len(self.myList)
    def add(self, elem):
        """
    Adds the elem to one end of the container list, keeping the end
    you add to consistent. Does not return anything
    """
        self.myList.append(elem)
class Stack(Container):
        """
    A subclass of Container. Has an additional method to remove elements.
    """
        def remove(self):
            """
    The newest elementn i the container list is removed
    Returns the element removed or None if the queue contains no elements
    """
            if self.size() > 0:
                last_elem=self.myList.pop(-1)
                last_elem *= 5
                return last_elem