from discord.ext import commands
from replit import db



# <-------------------[COG OTHER]--------------------> #

class cogOther(commands.Cog):



  def __init__(self, bot):    
    self.bot = bot

    
   
  # <-------------------[CMD PING]-------------------> #

  @commands.command(
    name = 'ping',
    description = "Check the ping.",
    aliases = []
  )
  async def cmdPing(self, ctx):

    import time

    start = time.perf_counter()
    msg = await ctx.send(content="Pinging...")
    end = time.perf_counter()
    t_t = (end - start) * 1000
    await msg.edit(content="Pong! {:.2f}ms".format(t_t))

    return

  
  
  # <-----------------[CMD DBSETUP]------------------> #

  @commands.command(
    name = 'dbsetup',
    description = "Setup or reset settings database.",
    aliases = []
  )
  @commands.is_owner()
  async def cmdSetup(self, ctx):

    db['settings'] = {}

    content = f"**⚙️  |  {ctx.author.name}**, settings database has undergone first setup or full reset."

    await ctx.send(content=content)

    return



# adds the Other commands to the bot
def setup(bot):
  bot.add_cog(cogOther(bot))
