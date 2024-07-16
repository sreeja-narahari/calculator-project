def add(num_1, num_2):
  return num_1 + num_2

def sub(num_1, num_2):
  return num_1 - num_2

def multiply(num_1, num_2):
  return num_1 * num_2

def divide(num_1, num_2):
  return num_1 / num_2
  
operations = {
  "+": add,
  "-": sub,
  "*": multiply,
  "/": divide
}

def calculator():

  from art import logo
  print(logo)

  num_1 = float(input("What's the first number?:  "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation:  ")
    num_2 = float(input("What's the next number?  "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num_1 = num_1, num_2 = num_2)
    
    print(f"{num_1} {operation_symbol} {num_2} = {answer}")
    
    next_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ").lower()
    
    if next_operation == 'y':
      num_1 = answer
    else:
      should_continue = False
      calculator()

calculator()