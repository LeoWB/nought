import run.values as values, run.interpreter as interp, run.environment as env
import front.ast as ast

def evaluateProgram(program: ast.Program, envr: env.Environment) -> values.RuntimeValue:
  lastEvaluated = values.NullValue()

  for statement in program.body: 
    lastEvaluated = interp.evaluate(statement, envr)
  # Loop through every statement in the program and evaluate it

  return lastEvaluated
  # Return the last statement evaluated

def evaluateVariableDeclaration(declaration: ast.VariableDeclaration, envr: env.Environment) -> values.RuntimeValue:
  return envr.declareVariable(declaration.ident, interp.evaluate(declaration.value, envr))
# Evaluate the expression and store it in the variable