import sys
import traceback
from discord.ext import commands



# <-------------------[COG ERROR]--------------------> #

class cogError(commands.Cog):



  def __init__(self, bot):
    self.bot = bot

  

  # <----------------[LISTENER ERROR]----------------> #

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):

    """
    The event triggered when an error is raised while invoking a command.

    Parameters
    ----------
    ctx: commands.Context
      The context used for command invocation
    error: commands.CommandError
      The Exception raised
      
    """

    # <----------[ERROR COMMAND NOT FOUND]-----------> #

    if isinstance(error, commands.CommandNotFound):

      pass



    # <-----------[ERROR COMMAND DISABLED]-----------> #

    elif isinstance(error, commands.DisabledCommand):

      content = f"**🔒  |  {ctx.author.display_name}**, that command is currently disabled."

      await ctx.send(content=content)



    # <----------[ERROR PERMISSIONS MISSING]----------> #
    
    elif isinstance(error, commands.MissingPermissions):
      
      content = f"‍🚓**  |  {ctx.author.display_name}**, you do not have the necessary permissions, try asking a mod."
      
      await ctx.send(content=content)  



    # <-----------[ERROR ARGUMENT MISSING]-----------> #

    elif isinstance(error, commands.MissingRequiredArgument):

      if ctx.command.qualified_name == 'graph':
        
        content = f"**☹️  |  {ctx.author.display_name}**, you are missing one or a combination of an equation, lower bound and upper bound for x. The syntax is `.graph <equation> <lower> <upper>`"

      elif ctx.command.qualified_name == 'limit':

        content = f"**☹️  |  {ctx.author.display_name}**, you are missing one or both an equation and a x-value to find the limit of. The syntax is `{ctx.prefix}limit <equation> <x-value>`"

      elif ctx.command.qualified_name in ['display', 'derive', 'integrate', 'solve']:

        content = f"☹️**  |  {ctx.author.display_name}**, you need to specify an equation."

      elif ctx.command.qualified_name in ['expand', 'factor', 'simplify', 'calculate']:

        content = f"☹️**  |  {ctx.author.display_name}**, you need to specify an expression."

      elif ctx.command.qualified_name == 'average':

        content = f"☹️**  |  {ctx.author.display_name}**, you need to specify a set of numbers separated by a space."

      elif ctx.command.qualified_name == 'prefix':

        content = f"**☹️  |  {ctx.author.display_name}**, you are missing what to change the prefix to."

      await ctx.send(content=content)
        


    # <-------------[ERROR ARGUMENT BAD]-------------> #
    
    elif isinstance(error, commands.BadArgument):

      if ctx.command.qualified_name == 'graph':

        content = f"**☹️  |  {ctx.author.display_name}**, the lower and upper bounds for x have to be numbers."

      elif ctx.command.qualified_name == 'limit':

        content = f"**☹️  |  {ctx.author.display_name}**, the x-value has to be a number."

      elif ctx.command.qualified_name == 'average':

        content = f"**☹️  |  {ctx.author.display_name}**, your input is not a set of numbers separated by a space."

      await ctx.send(content=content)


    # <---------------[Error Pythonic]---------------> #
    
    elif type(error.original) == SyntaxError:

      content = f"**☹️  |  {ctx.author.display_name}**, your input has led to an `Syntax Error`."

      await ctx.send(content=content)

    elif type(error.original) == OverflowError:

      content = f"**☹️  |  {ctx.author.display_name}**, your input has led to an `Overflow Error`."

      await ctx.send(content=content)

    elif type(error.original) == KeyError:

      content = f"**☹️  |  {ctx.author.display_name}**, your input can only involve the variable `x`."

      await ctx.send(content=content)
      
    else:
      
      print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
      traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    return



def setup(bot):
  bot.add_cog(cogError(bot))
