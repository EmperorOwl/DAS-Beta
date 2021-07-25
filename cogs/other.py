import discord
from discord.ext import commands
from replit import db



# <-------------------[COG OTHER]--------------------> #

class cogOther(commands.Cog):



  def __init__(self, bot):    
    self.bot = bot

  

  # <------------------[CMD ABOUT]-------------------> #

  @commands.command(
    name = 'about',
    description = "Check out some stats!"
  )
  async def cmdAbout(self, ctx):

    from modules.about import getAboutEmbed

    embed = getAboutEmbed(ctx)

    await ctx.send(embed=embed)
  
    return
   

  
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

  
  
  # <------------------[CMD INVITE]------------------> #

  @commands.command(
    name = 'invite',
    description = "Add Quirky to another server.",
    aliases = []
  )
  async def cmdInvite(self, ctx):

    embed = discord.Embed(
      title = "Thanks for using DAS!",
      description = "To add the bot to another server, click [here](https://discord.com/oauth2/authorize?client_id=863295366023086090&permissions=322624&scope=bot).",
      color = discord.Colour.blue()
    )

    await ctx.send(embed=embed)

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
