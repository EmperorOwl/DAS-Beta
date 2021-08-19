import discord
from discord.ext import commands
from datetime import datetime



# <------------------[COG HELP]-------------------> #

class cogHelp(commands.Cog):



  def __init__(self, bot):    
    self.bot = bot
    self.bot.remove_command('help') # removes default help command

  

  # <-----------------[CMD HELP]------------------> #

  @commands.command(
    name = 'help',
    description = "View the help page!",
    aliases = ['commands', 'cmds']
  )
  async def cmdHelp(self, ctx):

    from storage import bot_version

    embed = discord.Embed(
      title = 'Help Page',
      description = (
        f"*The Discord Algebra System (DAS) is a high quality calculator that supports TeX rendering and graphing to enhance the study of mathematics via Discord.*"
      ),
      color = discord.Colour.blue(),
      timestamp = datetime.now()
    )

    maths_cog = ctx.bot.get_cog('cogMaths')
    maths_cmds = maths_cog.get_commands()
    
    embed.add_field(
      name = 'My Commands',
      value = (
        '\n'.join(f"`{ctx.prefix}{cmd.name}` - {cmd.description}" for cmd in maths_cmds)
      )
    )

    cog_other = ctx.bot.get_cog('cogOther')
    other_cmds = list(cog_other.get_commands())[:-1] # remove owner only command
  
    embed.add_field(
      name = 'Other Commands',
      value = f" ".join(f'`{ctx.prefix}{c.name}` ' for c in other_cmds),
      inline = False
    )

    embed.set_thumbnail(url=ctx.bot.user.avatar_url)

    embed.set_footer(text=f'Version {bot_version}')

    await ctx.send(embed=embed)

    return



def setup(bot):
  bot.add_cog(cogHelp(bot))