import art

def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

operation = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
  
}

def calculator():
  print(art.logo)
  num1 = float(input("What's the first number?: "))


  for operator in operation:
   print(operator)
  condition = True
  while (condition):
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    calculation_function = operation[operation_symbol]
    first_answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    user_option= input(f"Type 'y' to continue calculation with {first_answer}, or type 'n' to start new calculation.: ")
    if(user_option == 'y'):
      condition = True
      num1 = first_answer
    elif(user_option == 'n'):
      condition = False
      calculator()


calculator()


  



  