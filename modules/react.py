import asyncio



# <-----------------[ADD REACTIONS]------------------> #

async def addReactions(ctx, message):

  await message.add_reaction('📈')
  await message.add_reaction('🗑️')
  await message.add_reaction('✅')

  while True:

    def check(reaction, user):
      return (reaction.message.id == message.id 
        and user.name != ctx.bot.user.name)

    try: 

      reaction, user = await ctx.bot.wait_for(
        'reaction_add', 
        timeout = 120,
        check = check
      )

      emoji = str(reaction)
      await message.remove_reaction(reaction, user)

      if emoji == '📈':

        await ctx.invoke(
          ctx.bot.get_command('graph'),
          equation = ctx.kwargs['equation'],
          lower = -5,
          upper = 5
        )

      elif emoji == '🗑️':

        await message.delete()
        await ctx.message.delete()

        return

      elif emoji == '✅':

        await ctx.message.delete()
        await message.clear_reactions()

        return

    except asyncio.TimeoutError:
        
      await message.clear_reactions()
      break

  return
