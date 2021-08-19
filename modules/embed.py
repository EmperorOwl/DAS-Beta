import discord
from datetime import datetime



# <---------------[GET MATH EMBED]----------------> #

def getThemedEmbed(ctx, equation, time_taken):

  if ctx.command.name == 'display':
    form = 'Display'
  elif ctx.command.name == 'limit':
    form = 'Limit'
  elif ctx.command.name == 'derive':
    form = 'Derivative'
  elif ctx.command.name == 'integrate':
    form = 'Integral'
  elif ctx.command.name == 'solve':
    form = 'Solution'
  elif ctx.command.name == 'expand':
    form = 'Expansion'
  elif ctx.command.name == 'factor':
    form = 'Factorisation'
  elif ctx.command.name == 'simplify':
    form = 'Simplification'

  embed = discord.Embed(
    title = f"{ctx.author.display_name}'s {form}",
    description = (
      f"Equation: `{equation}`\n"
      f"Syntax: `.{ctx.command.name} <equation>`\n"
      f"Time taken: `{time_taken}s`"
    ),
    timestamp = datetime.now(),
    color = discord.Colour.blue()
  )

  embed.set_image(url='attachment://tex.png')
  embed.set_footer(text=f'Powered by Matplotlib')

  return embed