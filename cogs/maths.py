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

    
 
# adds the Maths commands to the bot
def setup(bot):
  bot.add_cog(cogMaths(bot))
