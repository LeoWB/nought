from front import parser
from run import interpreter, values, environment
import sys

def repl():
  _parser = parser.Parser()
  envr = environment.Environment(None, {})
  envr.declareVariable('true', values.BoolValue(True))
  envr.declareVariable('false', values.BoolValue(False)) # TODO: Make booleans immutible
  # Define global variables

  while True:
    source = input("-> ")

    if source == "exit":
      sys.exit(0)

    program = _parser.produceAST(source)

    result = interpreter.evaluate(program, envr)
    print("result: ", vars(result))

repl()