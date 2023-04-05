from enum import Enum

# NodeType enumerator

class NodeType(Enum):
  # Statements
  PROGRAM = 0 
  VARDEC = 1 # Variable declaration

  # Expressions
  NUMERICLITERAL = 2
  IDENTIFIER = 3
  BINARYEXP = 4 # Binary expression
  CALLEXP = 5 # Call expression
  UNARYEXP = 6 # Unary expression
  FUNCDEC = 7 # Function declaration

# Statement class

class Statement:
  def __init__(self, kind: NodeType):
    self.kind = kind

# Expression extends Statement class 

class Exp(Statement):
  pass

# Program extends Statement class 
  
class Program(Statement):
  def __init__(self, body: list):
    super().__init__("PROGRAM")
    self.body = body

  def __str__(self) -> str:
    return "Program : \n{\n\tbody : " + str(self.body) +  "\n}"

# Variable Declaration extends Statement class 
  
class VariableDeclaration(Statement):
  def __init__(self, ident: str, value: Exp):
    super().__init__("VARDEC")
    self.ident = ident
    self.value = value

# Binary Expression extends Expression class 

class BinaryExp(Exp):
  def __init__(self, left: Exp, right: Exp, operator: str):
    super().__init__("BINARYEXP")
    self.left = left
    self.right = right
    self.operator = operator

  def __str__(self) -> str:
    return vars(self)

# Identifier extends Expression class 

class Identifier(Exp):
  def __init__(self, symbol: str):
    super().__init__("IDENTIFIER")
    self.symbol = symbol

# Numericliteral extends Expression class 

class NumericLiteral(Exp):
  def __init__(self, value: int):
    super().__init__("NUMERICLITERAL")
    self.value = value