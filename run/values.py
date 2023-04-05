from enum import Enum

# ValueType enumerator

class ValueType(Enum):
  NULL = 0
  NUM = 1 # Number

# RuntimeValue class

class RuntimeValue:
  def __init__(self, type: ValueType):
    self.type = type

# NumberValue extends RuntimeValue class

class NumberValue(RuntimeValue):
  def __init__(self, value: int): 
    super().__init__("number")
    self.value = value

# NumllValue extends RuntimeValue class

class NullValue(RuntimeValue):
  def __init__(self, value: None = None):
    super().__init__("null")
    self.value = value

# BoolValue extends RuntimeValue class

class BoolValue(RuntimeValue):
  def __init__(self, value: bool):
    super().__init__("bool")
    self.value = value