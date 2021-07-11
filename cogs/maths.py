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

    
 
# adds the Maths commands to the bot
def setup(bot):
  bot.add_cog(cogMaths(bot))
