import front.ast as ast # Abstract Syntax Tree
import front.lexer as lexer # Lexer includes functions and classes to create tokens
import sys 

# Parser class

class Parser:
  def __init__(self):
    self.tokens = [] # The parser class has one attribute: the list of tokens passed from the lexer

  def notEOF(self) -> bool:   
    return self.tokens[0].type != lexer.TokenType.EOF
  # If the current token's type is not an end-of-file type, return true
  
  def at(self) -> lexer.Token:
    return self.tokens[0]
  # Return the current token
  
  def eat(self) -> lexer.Token:
    previous = lexer.shift(self.tokens)
    return previous
  # Remove the current (first) token in the list but return it
  
  def expect(self, type: lexer.TokenType, error: str):
    previous = lexer.shift(self.tokens)
    if not previous or previous.type != type:
      print(f"{error} -> {previous}, expecting {type}")
      sys.exit(1)
  # If the previous token does not match an expected type, raise an error

  # ---------------------------------------------------- #
  
  def produceAST(self, source: str) -> ast.Program:
    self.tokens = lexer.tokenise(source)
    program = ast.Program([])
    # The Parser tokens attribute is set to the output of the lexer
    # A new program is created

    while self.notEOF():
      program.body.append(self.parseStatement())
    # Parse the next statement and add it to the body

    return program
 
  def parseStatement(self) -> ast.Statement:
    if self.at().type == lexer.TokenType.VAR:
      return self.parseVariableDeclaration()
    else:
      return self.parseExpression()
  # Parse a variable if the current token is one

  def parseVariableDeclaration(self) -> ast.Statement:
    ident = self.eat()
    if self.at().type == lexer.TokenType.SEMI:
      return ast.VariableDeclaration(ident.value, None)
    # If the variable isn't given a value, set it to None
    self.expect(lexer.TokenType.EQU, SyntaxError("\nerror: expected the variable to be assigned a value"))
    # Expect an equals otherwise

    declaration = ast.VariableDeclaration(ident.value, self.parseExpression())
    self.expect(lexer.TokenType.SEMI, SyntaxError("\nerror: semicolon expected"))
    # Parse the declaration and expect a semicolon

    return declaration

  def parseExpression(self) -> ast.Exp:
    return self.parseAdditiveExpression()
  #
  
  def parseAdditiveExpression(self) -> ast.Exp:
    left = self.parseMultiplicitiveExpression()
    # Evaluate the left side for expressions with higher prescidence

    while self.at().value == '+' or self.at().value == '-':
      operator = self.eat().value
      right = self.parseMultiplicitiveExpression()
      left = ast.BinaryExp(left, right, operator)
    # Save the operator between numbers
    # Evaluate the right side for expressions with higher prescidence
    # Return the final binary expression
    
    return left
  
  def parseMultiplicitiveExpression(self) -> ast.Exp:
    left = self.parsePrimaryExpression()

    while self.at().value == '*' or self.at().value == '/' or self.at().value == '%':
      operator = self.eat().value
      right = self.parsePrimaryExpression()
      left = ast.BinaryExp(left, right, operator)
    
    return left
  # ^

  def parsePrimaryExpression(self) -> ast.Exp:
    token = self.at().type
    # Get the current token's type

    if token == lexer.TokenType.IDENT:
      return ast.Identifier(self.eat().value)
    # Return the identifier with its value

    elif token == lexer.TokenType.NUM:
      return ast.NumericLiteral(int(self.eat().value)) 
    # Return the number with its value

    elif token == lexer.TokenType.OPENPAREN:
      self.eat()
      value = self.parseExpression()
      self.expect(lexer.TokenType.CLOSEPAREN, SyntaxError("\nerror: missing bracket"))
    # Move to inside the brackets
    # Parse the expression inside
    # If the bracket is not closed, throw an error

      return value
    
    elif token == lexer.TokenType.SEMI:
      self.eat()
    # If the token is a semicolon, move past it

    else:
      raise RuntimeError(f"\nerror: unexpected token: {self.at()}")
      sys.exit(1)
    # If the token doesn't exist, raise an error

  # Handle orders of prescidence: 
  # Assignment
  # Member
  # Function call
  # Logical
  # Comparison
  # Additive
  # Multiplicative
  # Unary
  # Primary    