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
  

  
  # <------------------[CMD EXPAND]------------------> #

  @commands.command(
    name = 'expand',
    description = "Expand an expression!",
    aliases = []
  )
  async def cmdExpand(self, ctx, expression):
    
    from modules.maths import getExpansion

    start = datetime.now()
    getExpansion(expression)
    end = datetime.now()

    time_taken = (end - start).total_seconds()

    file = discord.File('tex.png')
    embed = getThemedEmbed(ctx, expression, time_taken)
    await ctx.send(file=file, embed=embed)

    return

  
  
  # <--------------[CMD FACTORISATION]---------------> #
  
  @commands.command(
    name = 'factor',
    description = "Factor an expression!",
    aliases = []
  )
  async def cmdFactor(self, ctx, expression):
    
    from modules.maths import getFactorisation

    start = datetime.now()
    getFactorisation(expression)
    end = datetime.now()

    time_taken = (end - start).total_seconds()

    file = discord.File('tex.png')
    embed = getThemedEmbed(ctx, expression, time_taken)
    await ctx.send(file=file, embed=embed)

    return
  

  
  # <-----------------[CMD SIMPLIFY]-----------------> #

  @commands.command(
    name = 'simplify',
    description = "Simplify an expression!",
    aliases = []
  )
  async def cmdSimplify(self, ctx, expression):

    from modules.maths import getSimplification

    start = datetime.now()
    getSimplification(expression)
    end = datetime.now()

    time_taken = (end - start).total_seconds()

    file = discord.File('tex.png')
    embed = getThemedEmbed(ctx, expression, time_taken)
    await ctx.send(file=file, embed=embed)

    return
  
  
  
  # <-----------------[CMD AVERAGE]------------------> #

  @commands.command(
    name = 'average',
    description = 'Find the mean of a set of numbers!',
    aliases = []
  )
  async def cmdAverage(self, ctx, *, nums):

    try: # check user has inputted numbers

      nums = [float(num) for num in nums.split(' ')]

    except ValueError:

      raise commands.BadArgument

    average = round(sum(nums) / len(nums), 2)

    content = f"🧮**  |  {ctx.author.name}**, average is `{average}`!"

    await ctx.send(content=content)

    return
  
  
  
  # <----------------[CMD CALCULATE]-----------------> #

  @commands.command(
    name = 'calculate',
    description = "Compute a calculation!",
    aliases = ['calc', 'math']
  )
  async def cmdCalculate(self, ctx, *, expression):
    
    from modules.maths import calcExpression

    answer = calcExpression(expression)
    content = f"🧮**  |  {ctx.author.name}**, answer is `{answer}`!"

    await ctx.send(content=content)

    return

  
  
  # <-------------------[CMD ATR]--------------------> #

  @commands.command(
    name = 'atr',
    description = "Toggle automatic tex recognition.",
    aliases = []
  )
  @commands.has_permissions(manage_messages=True)
  async def cmdATR(self, ctx):

    settings = db['settings']

    try: # user has toggled before

      atr = settings[str(ctx.guild.id)]['atr']

      if atr == True:
        
        settings.update({ctx.guild.id: {'atr': False}})

        content = f"⚙️**  |  {ctx.author.display_name}** has disabled automatic tex listening!"
      
      else:

        settings.update({ctx.guild.id: {'atr': True}})

        content = f"⚙️**  |  {ctx.author.display_name}** has enabled automatic tex listening!"

    except KeyError: # user's first time

      settings.update({ctx.guild.id: {'atr': True}})

      content = f"⚙️**  |  {ctx.author.display_name}** has enabled automatic tex listening!"

    await ctx.send(content=content)

    return
  
  
  
  # <-------------[LISTENER ON MESSAGE]--------------> #

  @commands.Cog.listener()
  async def on_message(self, message):

    settings = db['settings']

    if re.search('\$(.*)\$', message.content) != None:

      try: # check whether user has enabled atr

        atr = settings[str(message.guild.id)]['atr']

        if atr == True:

          renderTeX(message.content)

          await message.channel.send(
            content = f'**{message.author.display_name}**',
            file = discord.File('tex.png')
          )

      except KeyError:
        pass

    return
  
  
  
# adds the Maths commands to the bot
def setup(bot):
  bot.add_cog(cogMaths(bot))
