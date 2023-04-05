from enum import Enum
import sys

# TokenType enumerator

class TokenType(Enum):
  # Types
  NUM = 0 # Number
  IDENT = 1 # Identifier
  VAR = 2 # Variable

  # Symbols
  EQU = 3 # Equals
  OPENPAREN = 4 # Open parenthesis
  CLOSEPAREN = 5 # Close parenthesis
  BINOP = 6 # Binary Operator
  SEMI = 7 # Semicolon

  EOF = 8 # Signifies end of a file

Keywords = {

}

# Token class

class Token:
  def __init__(self, value: str, type: TokenType):
    self.value = value
    self.type = type

def shift(vector: list) -> str:
  currentChar = vector[0]
  vector.pop(0)
  return currentChar
  # Remove the first item in a list and return it

def isAlpha(source: str) -> bool:
  return source.upper() != source.lower()
  # Check if a string contains only letters in the alphabet

def isInt(source: str) -> bool:
  return '0' <= source[0] <= '9'
  # Check if a string contains numbers

def isSkippable(source: str) -> bool:
  return source == " " or source == "\n" or source == "\t" or source == "\r" # This doesn't work -> \t is two characters
  # Skip over unwanted characters

# ---------------------------------------------------- #

def tokenise(source: str) -> list:
  tokens = []
  _source = list(source) 

  while len(_source) > 0:
    if _source[0] == '(':
      tokens.append(Token(shift(_source), TokenType.OPENPAREN))
    elif _source[0] == ')':
      tokens.append(Token(shift(_source), TokenType.CLOSEPAREN)) 
    elif _source[0] == '+' or _source[0] == '-' or _source[0] == '*' or _source[0] == '/' or _source[0] == '%':
      tokens.append(Token(shift(_source), TokenType.BINOP)) 
    elif _source[0] == '=':
      tokens.append(Token(shift(_source), TokenType.EQU))
    elif _source[0] == ';':
      tokens.append(Token(shift(_source), TokenType.SEMI))

  # Build each token until the end of the string
            
    else: # Handle multicharacter tokens

      if isInt(_source[0]): # Build number token
        num = ""
        while len(_source) > 0 and isInt(_source[0]): # mb error on _source[0]?
          num += shift(_source)
        # For every next consecutive digit, add it to the number
                
        tokens.append(Token(num, TokenType.NUM))
            
      elif isAlpha(_source[0]): # Build identifier token
        ident = ""
        while len(_source) > 0 and isAlpha(_source[0]):
          ident += shift(_source)
        # For every next consecutive letter, add it to the identifier
                
        if ident not in Keywords: 
          tokens.append(Token(ident, TokenType.IDENT))
        # If the identifier is not a keyword, add a identifier token
        else:
          tokens.append(Token(ident, Keywords[ident]))
        # If the identifier is a keyword, add the specific keyword token

      elif _source[0] == '$': # Handle variables
        shift(_source)
        ident = ""
        while len(_source) > 0 and isAlpha(_source[0]):
          ident += shift(_source)
        # For every next consecutive letter, add it to the variable name
                
        if ident == '':
          raise SyntaxError("\nerror: variable name not given")
        # Raise error if no variable name given
        
        tokens.append(Token(ident, TokenType.VAR))

      elif isSkippable(_source[0]):
        shift(_source)
      # Skip character, if skippable
            
      else:
        raise SyntaxError(f"\nerror: unrecognised character: {_source[0]}")
        sys.exit(1)
      # If the character fits no other category, raise an error

  tokens.append(Token("EndOfFile", TokenType.EOF))

  return tokens
