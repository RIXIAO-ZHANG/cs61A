"""
The behavior of repr is slightly more complicated than invoking __repr__ on its argument:
An instance attribute called __repr__ is ignored! Only class attributes are found.

The behavior of str is also complicated:
• An instance attribute called __str__ is ignored
• If no __str__ attribute is found, uses repr string
• (By the way, str is a class, not a function)
"""


def repr(expression):
    return type(expression).__repr__(expression)

def str(expression):
    class_type = type(expression)
    if hasattr(class_type, '__str__'):
        return  class_type.__str__(expression)
    return repr(expression)
