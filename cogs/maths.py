import discord
import re
from discord.ext import commands
from datetime import datetime
from replit import db



from modules.maths import renderTeX
from modules.embed import getThemedEmbed
from modules.react import addReactions



# <-------------------[COG MATHS]--------------------> #

class cogMaths(commands.Cog):



  def __init__(self, bot):
    self.bot = bot
    
  
  
  # <-----------------[CMD DISPLAY]------------------> #

  @commands.command(
    name = 'display',
    description = "Display an equation!",
    aliases = []
  )
  async def cmdDisplay(self, ctx, *, equation):

    start = datetime.now()
    renderTeX(f"${equation}$")
    end = datetime.now()

    time_taken = (end - start).total_seconds()

    file = discord.File('tex.png')
    embed = getThemedEmbed(ctx, equation, time_taken)
    message = await ctx.send(file=file, embed=embed)

    await addReactions(ctx, message)
    
    return

    
    
  # <------------------[CMD GRAPH]-------------------> #

  @commands.command(
    name = 'graph',
    description = "Plot the graph of an equation!",
    aliases = []
  )
  async def cmdGraph(self, ctx, equation, lower: float, upper: float):

    from modules.maths import plotGraph

    start = datetime.now()
    plotGraph(equation, lower, upper)
    end = datetime.now()

    embed = discord.Embed(
      title = f"{ctx.author.display_name}'s Graph",
      description = (
        f"Equation: `{equation}, x∈{lower, upper}`\n"
        f"Syntax: `.graph <eq> <lower> <upper>`\n"
        f"Time taken: `{(end-start).total_seconds()}s`"
      ),
      timestamp = datetime.now(),
      color = discord.Color.blue()
    )

    file = discord.File('graph.png')
    embed.set_image(url='attachment://graph.png')
    embed.set_footer(text='Powered by Matplotlib')

    await ctx.send(file=file, embed=embed)

    return
    
    
    
  # <------------------[CMD LIMIT]-------------------> #

  @commands.command(
    name = 'limit',
    description = "Find the limit of an equation!",
    aliases = []
  )
  async def cmdLimit(self, ctx, equation, x_value: float):

    from modules.maths import getLimit

    start = datetime.now()
    getLimit(equation, x_value)
    end = datetime.now()

    time_taken = (end - start).total_seconds()

    file = discord.File('tex.png')
    embed = getThemedEmbed(ctx, equation, time_taken)
    await ctx.send(file=file, embed=embed)

    return


  
  # <------------------[CMD DERIVE]------------------> #

  @commands.command(
    name = 'derive',
    description = "Derive an equation!",
    aliases = []
  )
  async def cmdDerive(self, ctx, equation):

    from modules.maths import getDerivative

    start = datetime.now()
    getDerivative(equation)
    end = datetime.now()

    time_taken = (end - start).total_seconds()

    file = discord.File('tex.png')
    embed = getThemedEmbed(ctx, equation, time_taken)
    await ctx.send(file=file, embed=embed)

    return
 


  # <-----------------[CMD INTEGRAL]-----------------> #

  @commands.command(
    name = 'integrate',
    description = "Integrate an equation!",
    aliases = []
  )
  async def cmdIntegrate(self, ctx, equation):

    from modules.maths import getIntegral

    start = datetime.now()
    getIntegral(equation)
    end = datetime.now()

    time_taken = (end - start).total_seconds()

    file = discord.File('tex.png')
    embed = getThemedEmbed(ctx, equation, time_taken)
    await ctx.send(file=file, embed=embed)

    return
  
  
  
  # <------------------[CMD SOLVE]-------------------> #

  @commands.command(
    name = 'solve',
    description = "Solve an equation!",
    aliases = []
  )
  async def cmdSolve(self, ctx, equation, domain='real'):
    
    from modules.maths import getSolution

    start = datetime.now()
    getSolution(equation, domain)
    end = datetime.now()

    time_taken = (end - start).total_seconds()

    file = discord.File('tex.png')
    embed = getThemedEmbed(ctx, equation, time_taken)
    await ctx.send(file=file, embed=embed)

    return
  
  

# adds the Maths commands to the bot
def setup(bot):
  bot.add_cog(cogMaths(bot))
