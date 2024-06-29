import discord
from discord import app_commands
from discord.ext import commands
import random
from ai import AI_bot


def read_bot_token():
  with open('../Tokens/BambooToken.txt', 'r') as file:
    return file.read().strip()


BOT_TOKEN = read_bot_token()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

async def dm_user(message):
  user = await bot.fetch_user(798267958270099557)
  await user.send(message)
  

@bot.event
async def on_ready():
  print("Hello world")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)
    

@bot.tree.command(name="dm_user", description="Dm a user in the server")
@app_commands.describe(user="Who would you like to dm?")
@app_commands.describe(message="What would you like to say?")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def dm_user(interaction: discord.Interaction, user: discord.Member, message: str):
  await interaction.response.send_message("I will now send that!", ephemeral=True)
  await user.send(message)
    
@bot.tree.command(name="send_message", description="Have me say something in a channel!")
@app_commands.describe(thing_to_say="what should I say?")
@app_commands.describe(channel="where should I send the message?")
@app_commands.default_permissions(manage_messages=True)
@app_commands.guild_only()
async def say(interaction: discord.Interaction, thing_to_say: str, channel: discord.TextChannel):
  await interaction.response.send_message("The message is sent", ephemeral=True)
  await channel.send(thing_to_say)
  
@bot.event
async def on_message(message):
  if message.channel.id != 1246554751659675718:
    conversation_exited = False
    # Check if the message is from the bot or not a ping
    if message.author == bot.user or not message.mentions.__contains__(bot.user):
      return
    await message.channel.send("""To exit this conversation say "exit" at any time.""")
    message_striped_ping = message.content.strip("<@1242325063588515870>")
    #question = f"Give a human like responce to this: {message_striped_ping}"
    answer = AI_bot(message_striped_ping)
    await message.reply(answer)
    while not conversation_exited:
      def check(response_message):
        return response_message.author == message.author and response_message.channel == message.channel

      try:
        user_response = await bot.wait_for('message', check=check)  # Wait for user response for 60 seconds
      except TimeoutError:
        await message.channel.send(
        "I didn't receive your response. If you want to talk, feel free to message me anytime!"
        )
      if user_response.content.lower() == "exit":
        await user_response.reply("Exiting the conversation now!", mention_author=False)
        conversation_exited = True
        break
      #question = f"Give a human responce to this: {user_response.content}"
      answer = AI_bot(user_response.content)
      await user_response.reply(answer)
      answer = ""
  
@bot.tree.command(name="redpandafact", description="Get a fun and insteresting fact about red pandas!!!")
@app_commands.guild_only()
async def redpandafact(interation: discord.Interaction):
  redpandafacts = []
  with open('redpandafacts.txt', 'r') as redpandafactslist:
    for fact in redpandafactslist:
      redpandafacts.append(fact.strip().strip('.'))
  index = random.randint(0, len(redpandafacts) - 1)
  await interation.response.send_message(redpandafacts[index])
  
@bot.tree.command(name="redpandafact_ai", description="Get a fun and insteresting fact about red pandas!!!")
@app_commands.guild_only()
async def redpandafact_ai(interation: discord.Interaction):
  question = "Give a fun fact about red pandas!"
  answer = AI_bot(question)
  await interation.response.send_message(answer)
  
  
@bot.tree.command(name="count", description="Have bamboo count!")
@app_commands.guild_only()
async def count(interation: discord.Interaction):
  if interation.channel_id == 1246554751659675718:
    counting_channel = await bot.fetch_channel(1246554751659675718)
    await interation.response.send_message("I will now count!", ephemeral=True)
    with open('../Bambeno/currentnumber.txt', 'r') as number:
      lines = number.readlines()
      for line in lines:
        number = line.strip()
        await counting_channel.send(int(number) + 1)
  else:
    await interation.response.send_message("Wrong channel for this command you have to use it in <#1246554751659675718>!", ephemeral=True)


      
bot.run(BOT_TOKEN)
