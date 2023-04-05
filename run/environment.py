import run.values as values

# Environment class

class Environment:
  def __init__(self, parent, variables): #: Environment, : dict
    self.parent = parent
    self.variables = variables

  def declareVariable(self, name: str, value: values.RuntimeValue) -> values.RuntimeValue:
    if name in self.variables:
      environment = self.resolve(name)
      environment.variables[name] = value
    
    self.variables[name] = value

    return value
  # Save a variable name to a value within a scope

  def lookupVariable(self, name: str) -> values.RuntimeValue:
    environment = self.resolve(name)
    return environment.variables[name]
  # Get the value of a certain variable by name

  def resolve(self, name: str):
    if name in self.variables:
      return self
    # Return the current environment if the given variable is in it
    
    if self.parent == None: # TODO: Check what value it would have if not None
      raise LookupError(f"\nerror: '{name}' does not exist in this scope")
    # If the variable is not in this scope, and there are no parent environments, it can't exist
  
    return self.parent.resolve(name)
