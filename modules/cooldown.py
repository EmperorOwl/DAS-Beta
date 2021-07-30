from discord.ext import commands



# <--------------[GET SHARED COOLDOWN]---------------> #

def getSharedCooldown():

  """
  Creates cooldown decorator for each command set at one user per five seconds per user.
  """
  
  cooldown = commands.Cooldown(
    rate = 1, 
    per = 5, 
    type = commands.BucketType.user)
  
  def decorator(func):
    if isinstance(func, commands.Command):
      func._buckets = commands.CooldownMapping(cooldown)
    else:
      func.__commands_cooldown__ = cooldown
    return func
  return decorator