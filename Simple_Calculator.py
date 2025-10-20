while True :
  def process(a,b,c) :
      if c == "+":
          return a+b
      elif c == "-":
          return a-b
      elif c == "*":
          return a*b
      elif c == "/":
          if b == 0:
              return "Undefined!"
          else:
              return a/b
      elif c == "**":
          return a**b
      elif c == "//":
          return a//b
      else:
          return "Choose the available transactions."

  transactions =process(a =float(input("Enter a number:")),
               b =float(input("Enter a second number:")),
               c =input("Select the action you want to perform(+,-,*,/,**,//):"))
  print(transactions)

