import discord
from discord.ext import commands
from discord.ext import tasks
import datetime

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

tz = datetime.datetime.now().astimezone().tzinfo     # local timezone
print('timezone:', tz)

midnight = datetime.time(hour=00, minute=00, second=0, microsecond=0, tzinfo=tz)
print('midnight:', midnight, midnight.tzinfo)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')
  dm_user.start("Hello!")

@tasks.loop(time=midnight)
async def dm_user(message):
  try:
    user = await bot.fetch_user(798267958270099557)
    await user.send(message)
    print(f'Sent DM to {user.name} ({user.id})')
  except discord.HTTPException as e:
    print(f'Failed to send DM: {e}')


# (Optional: Add other event listeners if needed)


if __name__ == '__main__':
  with open('token.txt', 'r') as f:
    token = f.read().strip()
  bot.run(token)
