import run.values as values, run.interpreter as interp, run.environment as env
import front.ast as ast

def evaluateBinaryExpression(binop: ast.BinaryExp, envr: env.Environment) -> values.RuntimeValue:
  left = interp.evaluate(binop.left, envr)
  right = interp.evaluate(binop.right, envr)
  # Evaluate the expressions on either side of the operator

  if left.type == "number" and right.type == "number":
    return evaluateNumericBinaryExpression(left, right, binop.operator)
  
  else:
    return values.NullValue()
  
def evaluateNumericBinaryExpression(
  left: values.NumberValue, 
  right: values.NumberValue, 
  operator: str
  ) -> values.NumberValue:
  result = 0
  
  if operator == '+':
    result = left.value + right.value
  elif operator == '-':
    result = left.value - right.value
  elif operator == '*':
    result = left.value * right.value
  elif operator == '/':
    result = left.value / right.value # Divison by zero later
  elif operator == '%':
    result = left.value % right.value

  return values.NumberValue(result)
# Evaluate the result of a numeric binary expression depending on the operator

def evaluateIdentifier(ident: ast.Identifier, envr: env.Environment) -> values.RuntimeValue:
  value = envr.lookupVariable(ident.symbol)
  return value
# Return the value of a identifier