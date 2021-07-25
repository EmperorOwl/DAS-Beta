import os
import replit
import discord
from discord.ext import commands
from replit import db



# <----------------[MATPLOTLIB SETUP]----------------> #

os.environ['MPLCONFIGDIR'] = os.getcwd()+"/configs/"



# <-----------------[INTENTS SETUP]------------------> #

intents = discord.Intents.default()

intents.members = True # enables bot to track number of servers and users who use the bot



# <------------------[PREFIX SETUP]------------------> #

def get_prefix(client, message):

  try: # search for custom prefix

    prefix = db['settings'][str(message.guild.id)]['prefix']

  except KeyError: # otherwise set default one

    prefix = '.'

  return prefix



# <-------------------[BOT SETUP]--------------------> #

bot = commands.Bot(

  case_insensitive = True,

  command_prefix = get_prefix,

)



# <------------------[BOT STARTUP]-------------------> #

@bot.event
async def on_ready():

  replit.clear() # clears terminal

  print(f"Logged in as {bot.user.name} - {bot.user.id}")
  
  bot.load_extension('cogs.maths')
  bot.load_extension('cogs.other')
  bot.load_extension('cogs.error')
  bot.load_extension('cogs.help')

  return

bot.run(os.environ['DISCORD_BOT_TOKEN'])
