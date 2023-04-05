import run.values as values, run.environment as env
import run.evaluation.expressions as exp, run.evaluation.statements as stmt
import front.ast as ast

def evaluate(astNode: ast.Statement, envr: env.Environment) -> values.RuntimeValue:
  node = astNode.kind
  if node == "NUMERICLITERAL":
    return values.NumberValue(astNode.value)
  
  elif node == "IDENTIFIER":
    return exp.evaluateIdentifier(astNode, envr)

  elif node == "BINARYEXP":
    return exp.evaluateBinaryExpression(astNode, envr)
  
  elif node == "PROGRAM":
    return stmt.evaluateProgram(astNode, envr)
  
  elif node == "VARDEC":
    return stmt.evaluateVariableDeclaration(astNode, envr)

  # Evaluate each AST node depending on its type

  else:
    raise RuntimeError("\nerror: AST node not supported: ", vars(astNode))
  # Raise an error if the node is not supported