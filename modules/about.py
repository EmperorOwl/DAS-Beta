import discord
import psutil
import sys



# <----------------[GET ABOUT EMBED]-----------------> #

def getAboutEmbed(ctx):

  from storage import bot_version

  per = psutil.virtual_memory().percent
  used = round(per / 100 * 4, 2)
  percent = round(used / 4 * 100, 2)
  memory = f'{used} GB used out of 4.00 GB ({percent}%)'
  latency = round(ctx.bot.latency*1000, 2)

  embed = discord.Embed(
    title = 'About Me',
    description = (

      "The Discord Algebra System (DAS) is a high quality calculator that supports TeX rendering and graphing to enhance the study of mathematics via Discord.\n"

      '\n'

      f"`      Developer:` EmperorOwl#4400\n"
      f"`        Servers:` {len(ctx.bot.guilds)}\n"
      f"`          Users:` {len(ctx.bot.users)}\n"
      f"`       Commands:` {len(ctx.bot.commands)}\n"
      f"`         Memory:` {memory}\n"
      f"`      CPU Usage:` {psutil.cpu_percent()}%\n"
      f"`        Latency:` {latency} ms\n"
      f"`    Bot Version:` {bot_version}\n"
      f"` Python Version:` {sys.version[:6]}\n"
      f"`       Platform:` Replit — Hacker (Always On + Boosted)\n"

      '\n'

      "[Top.gg Site](https://top.gg/bot/863295366023086090) ~ [Invite Me](https://discord.com/api/oauth2/authorize?client_id=863295366023086090&permissions=322624&scope=bot)"
      
    ),
    color = discord.Colour.blue()
  )

  return embed