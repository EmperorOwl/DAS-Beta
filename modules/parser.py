from sympy.parsing.sympy_parser import (
  parse_expr, # converts string to sympy expression
  standard_transformations, # eg. 5! = 5*4*3*2*1
  implicit_multiplication_application, # e.g. 2x = 2*x
  convert_xor # e.g. 2^x = 2**x
)



# <----------------[CHECK CHARACTERS]----------------> #

def checkTooManyCharacters(expression):

  if len(expression) > 14:

    raise OverflowError
  
  return expression



# <----------------[CHECK EXPONENTS]-----------------> #

def checkTooManyExponents(expression):

  """
  Deals with a strange issue, where bot stops responding when trying to process more than five exponents
  """

  exponents_list = expression.split('**')[1:]

  if len(exponents_list) > 0:

    for exponent in exponents_list:

      exponents = 0
      for character in exponent:
        if character not in ['+', '-', '*', '/']:
          exponents += 1
        else:
          break
        
      if exponents > 4:
        raise OverflowError

  return expression



# <----------------[PARSE EXPRESSION]----------------> #

def parseExpression(expression):

  expression = expression.replace('y=', '')
  expression = expression.replace('^', '**')
  expression = expression.replace('e', 'E')

  checkTooManyCharacters(expression)
  checkTooManyExponents(expression)
    
  transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))
  equation = parse_expr(expression, transformations=transformations)
  
  return equation