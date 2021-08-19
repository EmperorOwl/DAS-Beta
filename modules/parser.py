from sympy.parsing.sympy_parser import (
  parse_expr, # converts string to sympy expression
  standard_transformations, # eg. 5! = 5*4*3*2*1
  implicit_multiplication_application, # e.g. 2x = 2*x
  convert_xor # e.g. 2^x = 2**x
)



# <--------------[PARSE EXPRESSION]---------------> #

def parseExpression(expression):

  expression = expression.replace('y=', '')
  expression = expression.replace('^', '**')
  expression = expression.replace('e', 'E')
    
  transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))
  equation = parse_expr(expression, transformations=transformations)
  
  return equation