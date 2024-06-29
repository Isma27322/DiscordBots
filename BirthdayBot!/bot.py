import discord
from discord import app_commands
from discord.ext import commands
from webcolors import name_to_hex
from date import get_date
from discord.ext import tasks
import datetime
import random
import os

def read_bot_token():
  with open('../Tokens/BirthdayBotToken.txt', 'r') as file:
    return file.read().strip()

def get_hex_from_name(color_name):
  color_name_no_spaces = ""
  for char in color_name:
    if char != " ":
      color_name_no_spaces += char
  try:
    hex_code = name_to_hex(color_name_no_spaces).upper()  # Convert to uppercase for consistent format
    # Check if "#" exists and remove it before prepending "0x"
    if hex_code.startswith("#"):
      hex_code = hex_code[1:]  # Remove leading "#" if present
    return f"0x{hex_code}"  # Prepend "0x" without the "#"
  except ValueError:
    return None
  
tz = datetime.datetime.now().astimezone().tzinfo     # local timezone

midnight = datetime.time(hour=23, minute=00, second=0, microsecond=0, tzinfo=tz)

BOT_TOKEN = read_bot_token()
SERVER_NAMES = []
SERVER_IDS = []
REACTION_ROLES_CHANNEL = []
COUNTDOWN_CHANNEL = []
REACTION_ROLES = []
BIRTHDAY_ROLE = []
WELCOME_CHANNEL = []
PERSONAL_MESSAGES_CATEGORY = []
RULES_CHANNEL = []
CARD_CHANNEL = []
WISHES_CHANNEL = []
GIFTS_CHANNEL = []
MEMORIES_CHANNEL = []
ANNOUNCEMENT_CHANNEL = []
COUNTDOWNS = []
COUNTDOWN_ROLE = []

def get_server_names():
  with open('./StuffForKeeping/server_names.txt', 'r') as server_names_file:
    lines = server_names_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      SERVER_NAMES.append(line_striped)
    server_names_file.close()

def get_server_ids():
  with open('./StuffForKeeping/server_ids.txt', 'r') as server_ids_file:
    lines = server_ids_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      SERVER_IDS.append(line_striped)
    server_ids_file.close()

def get_reaction_roles_channel():
  with open('./StuffForKeeping/roles_channel.txt', 'r') as roles_channel_file:
    lines = roles_channel_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      REACTION_ROLES_CHANNEL.append(line_striped)
    roles_channel_file.close()

def get_countdown_channel():
  with open('./StuffForKeeping/countdown_channel.txt', 'r') as countdown_channel_file:
    lines = countdown_channel_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      COUNTDOWN_CHANNEL.append(line_striped)
    countdown_channel_file.close()

def get_birthday_role():
  with open('./StuffForKeeping/birthday_role.txt', 'r') as birthday_role_file:
    lines = birthday_role_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      BIRTHDAY_ROLE.append(line_striped)
    birthday_role_file.close()

def get_welcome_channel():
  with open('./StuffForKeeping/welcome_channel.txt', 'r') as welcome_channel_file:
    lines = welcome_channel_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      WELCOME_CHANNEL.append(line_striped)
    welcome_channel_file.close

def get_personal_messages_cat():
  with open('./StuffForKeeping/personal_messages_cat.txt','r') as personal_messages_cat_file:
    lines = personal_messages_cat_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      PERSONAL_MESSAGES_CATEGORY.append(line_striped)
    personal_messages_cat_file.close()

def get_rules_channel():
  with open('./StuffForKeeping/rules_channel.txt','r') as rules_channel_file:
    lines = rules_channel_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      RULES_CHANNEL.append(line_striped)
    rules_channel_file.close()

def get_card_channel():
  with open('./StuffForKeeping/card_channel.txt','r') as card_channel_file:
    lines = card_channel_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      CARD_CHANNEL.append(line_striped)
    card_channel_file.close()

def get_wishes_channel():
  with open('./StuffForKeeping/wishes_channel.txt','r') as wishes_channel_file:
    lines = wishes_channel_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      WISHES_CHANNEL.append(line_striped)
    wishes_channel_file.close()

def get_gifts_channel():
  with open('./StuffForKeeping/gifts_channel.txt','r') as gifts_channel_file:
    lines = gifts_channel_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      GIFTS_CHANNEL.append(line_striped)
    gifts_channel_file.close()

def get_memories_channel():
  with open('./StuffForKeeping/memories_channel.txt','r') as memories_channel_file:
    lines = memories_channel_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      MEMORIES_CHANNEL.append(line_striped)
    memories_channel_file.close()

def get_reaction_roles(server_name):
  reaction_roles_local = []
  with open(f'./StuffForKeeping/reactionroles/{server_name}_reaction_roles.txt', 'r') as reaction_roles_file:
    lines = reaction_roles_file.readlines()
    for line in lines:
      reaction_roles_local.append(line.strip())
    REACTION_ROLES.append(reaction_roles_local)
    reaction_roles_file.close()

def get_announcement_channel():
  with open('./StuffForKeeping/announcement_channel.txt','r') as announcement_channel_file:
    lines = announcement_channel_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      ANNOUNCEMENT_CHANNEL.append(line_striped)
    announcement_channel_file.close()
    
def get_countdowns():
  with open('./StuffForKeeping/coutdowns.txt', 'r') as coutdowns_file:
    lines = coutdowns_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      COUNTDOWNS.append(line_striped)
    coutdowns_file.close()
    
def get_coutdown_role():
  with open('./StuffForKeeping/coutdown_role.txt', 'r') as coutdown_role_file:
    lines = coutdown_role_file.readlines()
    for line in lines:
      line_striped = line.strip()
      if line_striped == '':
        continue
      COUNTDOWN_ROLE.append(line_striped)
    coutdown_role_file.close()
    

get_server_names()
get_server_ids()
get_reaction_roles_channel()
get_countdown_channel()
get_birthday_role()
get_welcome_channel()
get_personal_messages_cat()
get_rules_channel()
get_card_channel()
get_wishes_channel()
get_gifts_channel()
get_memories_channel()
get_announcement_channel()
get_countdowns()
get_coutdown_role()
for server in SERVER_NAMES:
  try:
    get_reaction_roles(server)
  except FileNotFoundError:
    pass


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Hello world")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
    countdown.start()
  except Exception as e:
    print(e)
    
    
@bot.tree.command(name="help", description="Get help for using the bot")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def help(interaction: discord.Interaction):
  await interaction.response.send_message("""First of all. If you don't already have the server set up or you would like the bot to set it up for you 
please run the /setup_server command, if you do that it will setup the channels categorys, and roles for you.
To get help with that command and get more info run the /setup_server_help

Then you should run the /setup_bot command to give the server stuff to the bot. 
To get help with that command run the /setup_bot_help command

To get help with seting up reaction roles run /roles_help

To get help with seting up the countdown run /countdown_help

And then the /create_personal_message command is usable by anyone(as long as you setup the category for it and tell the bot the category)
It is just used to create the channel for the personal message and assign proper access.

Also just a note is that for all the commands except for the create personal message command you need to have administrator or manage messages permisions to run the command
""", ephemeral=True)
  
@bot.tree.command(name="setup_bot_help", description="Get help for using the bot")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def setup_bot_help(interaction: discord.Interaction):
  await interaction.response.send_message("""
Ok so the setup bot command is for if you want to design the server yourself and just tell the bot the roles, channels and categories that it needs.

The things that it requests is
1. The reaction roles channel aka where people go to get their roles.
2. Coutdown channel aka the channel where the countdown will happen 
3. Welcome channel aka where the bot will send the welcome messages for when people join.
4. Birthday role aka the role you setup for the person that this birthday server is for
5. Coutdown role aka the role that is pinged with the coutdown
6. The card channel aka the channel where people sign the birthday card.
7. Wishes_channel aka the channel where people send birthday wishes for their birthday
8. Announcement channel aka the channel where announcements can be made.
9. Peronal messages category aka the category that is used for personal messages(optional)
10. Rules channel aka the channel that holds the rules for this server.(Optional)
11. Gifts channel aka the channel that is used for people to send gifts(Optional)
""", ephemeral=True)
  

@bot.tree.command(name="setup_server_help", description="Get help for using the bot")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def setup_server_help(interaction: discord.Interaction):
  await interaction.response.send_message("""So to have the bot setup the entire server for you is really easy to run.
                                          
It only requests two things, the gender of the birthday person and then their favorite color.

Then it will setup the channels, categorys and some roles for you!

The roles that it will setup for you are:
Countdown, Announcements, Co-worker, Friend, Bestie, Former, Low Rank, Middle Rank, High Rank, and Senior Rank
""", ephemeral=True)


@bot.tree.command(name="roles_help", description="Get help for using the bot")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def roles_help(interaction: discord.Interaction):
  await interaction.response.send_message("""So first of all, First of all. You need to make sure that you have eather setup the server or setup the bot with this server or it won't work.

Then to setup the roles you need to run the /setup_roles command and say how many roles you want to setup, 

then the bot will ask you a series of questions related to the reaction roles.

First being what the reaction roles are for, example: Notification Roles, etc.

Then it will ask you if you wan to add what the roles are for or not(It is up to you!).

Then it will ask for the emoji for the role for the users to react on the message to get the role.

The emoji MUST be a discord emoji or a emoji that is in this server or it won't work.

Then the name of the role for that emoji you just gave the bot
Then it will ask the questions for the emojis the role name and the what the role is for(If you said yes)

You can do more than one message for reaction roles so you don't need to fit it all in one.

Also there is a one minute max for each input.

""", ephemeral=True)


@bot.tree.command(name="countdown_help", description="Get help for using the bot")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def countdown_help(interaction: discord.Interaction):
  await interaction.response.send_message("""
To setup and start the countdown run /countdown with the amount of days untill their birthday.

Then the bot will respond back with the date based on that to confirm that it is the correct date.

If it is not then just reply with no and it will ask for the days untill their birthday again untill you get the correct date.   
                              
Note for countdown command if it just dosen't respond it means what I am using errored out and didin't work. 

I don't really know how to fix it so just run the command again.
""", ephemeral=True)


@bot.tree.command(name="setup_server", description="Have the bot set up the server for you!")
@app_commands.describe(gender="What gender is the birthday person? Male, female, or non binary")
@app_commands.choices(gender=[
    discord.app_commands.Choice(name="Male", value=1),
    discord.app_commands.Choice(name="Female", value=2),
    discord.app_commands.Choice(name="Non Binary", value=3)
])
@app_commands.describe(favcolor="What is that persons favorite color?(Please make sure that it is spelled correctly)")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def setup_server(interaction: discord.Interaction, gender: discord.app_commands.Choice[int], favcolor: str):
  if interaction.guild.name in SERVER_NAMES:
    await interaction.response.send_message("This server is already setup in the bot you don't need to do it again.", ephemeral=True)
  else:  
    BirthdayPersonGender = gender.name
    await interaction.response.send_message("I will now setup the server for you please stand by.", ephemeral=True)
    guild = interaction.guild
    birthday_role = ""
    welcome_channel = await guild.create_text_channel("Welcome!", topic="Welcomeing new users!")
    announcement_channel = await guild.create_text_channel("Announcements", topic="Read announcements related to the birthday!")
    countdown_channel = await guild.create_text_channel("Countdown", topic="Countdown till their birthday")
    roles_channel = await guild.create_text_channel("Roles", topic="Get your roles here!")
    rules_channel = await guild.create_text_channel("Rules", topic="View the rules for this server here!")
    await guild.create_category("Community")
    general_category = discord.utils.get(guild.categories, name="Community")
    await guild.create_text_channel("General", topic="General Chat", category=general_category)
    await guild.create_text_channel("Commands", topic="For running commands", category=general_category)
    await guild.create_category("Birthday stuff")
    birthday_category = discord.utils.get(guild.categories, name="Birthday stuff")
    card_channel = await guild.create_text_channel("Birthday card", topic="Sign the birthday card!", category=birthday_category)
    wishes_channel = await guild.create_text_channel("Birthday wishes", topic="Give a wish for their birthday!", category=birthday_category)
    gifts_channel = await guild.create_text_channel("Birthday gifts", topic="Give them a gift for them to enojoy on their birthday", category=birthday_category)
    memories_channel = await guild.create_text_channel("Memories", topic="Share some of your memories with them!", category=birthday_category)
    personal_messages_category = await guild.create_category("Personal Messages")
    hex_color = get_hex_from_name(favcolor)
    color = discord.Colour(int(hex_color, 16))
    if BirthdayPersonGender == "Male":
      birthday_role = await guild.create_role(name="Birthday Boy!", mentionable=True, color=color)
    elif BirthdayPersonGender == "Female":
      birthday_role = await guild.create_role(name="Birthday Girl!", mentionable=True, color=color)
    elif BirthdayPersonGender == "Non Binary":
      birthday_role = await guild.create_role(name="Birthday Person!", mentionable=True, color=color)
    else:
      print("This is somehow not working")
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    countdown_role = await guild.create_role(name="Countdown", mentionable=True, color=random_color)
    
    
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    await guild.create_role(name="Announcements", mentionable=True, color=random_color)
    
    
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    await guild.create_role(name="Co-worker", mentionable=True, color=random_color)
    
    
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    await guild.create_role(name="Friend", mentionable=True, color=random_color)
    
    
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    await guild.create_role(name="Bestie", mentionable=True, color=random_color)
    
    
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    await guild.create_role(name="Former", mentionable=True, color=random_color)
    
    
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    await guild.create_role(name="Low Rank", mentionable=True, color=random_color)
    
    
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    await guild.create_role(name="Middle Rank", mentionable=True, color=random_color)
    
    
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    await guild.create_role(name="High Rank", mentionable=True, color=random_color)
    
    random_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))
    await guild.create_role(name="Senior Rank", mentionable=True, color=random_color)
    
    
    SERVER_NAMES.append(guild.name)
    with open('./StuffForKeeping/server_names.txt', 'a') as server_names_file:
      server_names_file.write(f"\n{guild.name}")
      server_names_file.close()
    
    
    SERVER_IDS.append(guild.id)
    with open('./StuffForKeeping/server_ids.txt', 'a') as server_ids_file:
      server_ids_file.write(f"\n{guild.id}")
      server_ids_file.close()
      
    
    WELCOME_CHANNEL.append(guild.name)
    WELCOME_CHANNEL.append(welcome_channel.id)
    with open('./StuffForKeeping/welcome_channel.txt', 'a') as welcome_channel_file:
      welcome_channel_file.write(f"\n{guild.name}")
      welcome_channel_file.write(f"\n{welcome_channel.id}")
      welcome_channel_file.close()
    
    
    COUNTDOWN_CHANNEL.append(guild.name)
    COUNTDOWN_CHANNEL.append(countdown_channel.id)
    with open('./StuffForKeeping/countdown_channel.txt', 'a') as countdown_channel_file:
      countdown_channel_file.write(f"\n{guild.name}")
      countdown_channel_file.write(f"\n{countdown_channel.id}")
      countdown_channel_file.close()
      
    
    REACTION_ROLES_CHANNEL.append(guild.name)
    REACTION_ROLES_CHANNEL.append(roles_channel.id)
    with open('./StuffForKeeping/roles_channel.txt', 'a') as roles_channel_file:
      roles_channel_file.write(f"\n{guild.name}")
      roles_channel_file.write(f"\n{roles_channel.id}")
      roles_channel_file.close()


    BIRTHDAY_ROLE.append(guild.name)
    BIRTHDAY_ROLE.append(birthday_role.name)
    with open('./StuffForKeeping/birthday_role.txt', 'a') as birthday_role_file:
      birthday_role_file.write(f"\n{guild.name}")
      birthday_role_file.write(f"\n{birthday_role.name}")
      birthday_role_file.close()


    PERSONAL_MESSAGES_CATEGORY.append(guild.name)
    PERSONAL_MESSAGES_CATEGORY.append(personal_messages_category.name)
    with open('./StuffForKeeping/personal_messages_cat.txt', 'a') as personal_messages_cat_file:
      personal_messages_cat_file.write(f"\n{guild.name}")
      personal_messages_cat_file.write(f"\n{personal_messages_category.name}")
      personal_messages_cat_file.close()

      
    RULES_CHANNEL.append(guild.name)
    RULES_CHANNEL.append(rules_channel.id)
    with open('./StuffForKeeping/rules_channel.txt', 'a') as rules_channel_file:
      rules_channel_file.write(f"\n{guild.name}")
      rules_channel_file.write(f"\n{rules_channel.id}")
      rules_channel_file.close()
      
    
    CARD_CHANNEL.append(guild.name)
    CARD_CHANNEL.append(card_channel.id)
    with open('./StuffForKeeping/card_channel.txt', 'a') as card_channel_file:
      card_channel_file.write(f"\n{guild.name}")
      card_channel_file.write(f"\n{card_channel.id}")
      card_channel_file.close()
      
    
    WISHES_CHANNEL.append(guild.name)
    WISHES_CHANNEL.append(wishes_channel.id)
    with open('./StuffForKeeping/wishes_channel.txt', 'a') as wishes_channel_file:
      wishes_channel_file.write(f"\n{guild.name}")
      wishes_channel_file.write(f"\n{wishes_channel.id}")
      wishes_channel_file.close()
      
    
    GIFTS_CHANNEL.append(guild.name)
    GIFTS_CHANNEL.append(gifts_channel.id)
    with open('./StuffForKeeping/gifts_channel.txt', 'a') as gifts_channel_file:
      gifts_channel_file.write(f"\n{guild.name}")
      gifts_channel_file.write(f"\n{gifts_channel.id}")
      gifts_channel_file.close()
      
    
    MEMORIES_CHANNEL.append(guild.name)
    MEMORIES_CHANNEL.append(memories_channel.id)
    with open('./StuffForKeeping/memories_channel.txt', 'a') as memories_channel_file:
      memories_channel_file.write(f"\n{guild.name}")
      memories_channel_file.write(f"\n{memories_channel.id}")
      memories_channel_file.close()
      
    
    ANNOUNCEMENT_CHANNEL.append(guild.name)
    ANNOUNCEMENT_CHANNEL.append(announcement_channel.id)
    with open('./StuffForKeeping/announcement_channel.txt', 'a') as announcement_channel_file:
      announcement_channel_file.write(f"\n{guild.name}")
      announcement_channel_file.write(f"\n{announcement_channel.id}")
      announcement_channel_file.close()
      
    COUNTDOWN_ROLE.append(guild.name)
    COUNTDOWN_ROLE.append(countdown_role.name)
    with open('./StuffForKeeping/coutdown_role.txt', 'a') as coutdown_role_file:
      coutdown_role_file.write(f"\n{guild.name}")
      coutdown_role_file.write(f"\n{countdown_role.name}")
      coutdown_role_file.close()

  

@bot.tree.command(name="remove_channels_and_categ", description="Remove channels and categories. For testing only!")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def remove_channels_and_categ(interaction: discord.Interaction):
  await interaction.response.send_message("Please stand by as I do that!", ephemeral=True)
  guild = interaction.guild
  categoryTemp = discord.utils.get(guild.categories, name="Test")
  categoryBirthday = discord.utils.get(guild.categories, name="Birthday stuff")
  categoryGeneral = discord.utils.get(guild.categories, name="Community")
  categoryPersMess = discord.utils.get(guild.categories, name="Personal Messages") 
  TempChannels = categoryTemp.channels
  BirthdayChannels = categoryBirthday.channels
  GeneralChannels = categoryGeneral.channels
  PersMessChannels = categoryPersMess.channels
  for channel in TempChannels: # We search for all channels in a loop
    try:
      await channel.delete() # Delete all channels
    except AttributeError: # If the category does not exist/channels are gone
      pass
  for channel in BirthdayChannels: # We search for all channels in a loop
    try:
      await channel.delete() # Delete all channels
    except AttributeError: # If the category does not exist/channels are gone
      pass
  for channel in GeneralChannels: # We search for all channels in a loop
    try:
      await channel.delete() # Delete all channels
    except AttributeError: # If the category does not exist/channels are gone
      pass
  for channel in PersMessChannels: # We search for all channels in a loop
    try:
      await channel.delete() # Delete all channels
    except AttributeError: # If the category does not exist/channels are gone
      pass
  await categoryTemp.delete()
  await categoryBirthday.delete()
  await categoryGeneral.delete()
  await categoryPersMess.delete()



@bot.tree.command(name="setup_bot", description="Setup the bot on this server")
@app_commands.describe(reaction_roles = "Where are the reaction roles for this server?")
@app_commands.describe(countdown_channel = "Where is the birthday countdown for this server?")
@app_commands.describe(welcome_channel="What channel would you like the people who are first joining to be sent in?")
@app_commands.describe(birthday_role="What is the role for the birthday person at this server?")
@app_commands.describe(countdown_role="What role is used to ping for the countdown?")
@app_commands.describe(personal_messages="What category are the personal messages in?(optional)")
@app_commands.describe(card_channel="What channel will the card signing happen?")
@app_commands.describe(wishes_channel="What channel will people send their wishes?")
@app_commands.describe(memories_channel="What channel will people use to send their memories?")
@app_commands.describe(rules_channel="What channel is used for the rules?(optional)")
@app_commands.describe(gifts_channel="What channel is used for sending gifts?(optional)")
@app_commands.describe(announcement_channel="What channel is used for announcements?")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def setup_bot(interaction: discord.Interaction, reaction_roles: discord.TextChannel, countdown_channel: discord.TextChannel
  , welcome_channel: discord.TextChannel, birthday_role: discord.Role, countdown_role: discord.Role, card_channel: discord.TextChannel, 
  wishes_channel: discord.TextChannel, memories_channel: discord.TextChannel, announcement_channel: discord.TextChannel,
  personal_messages: discord.CategoryChannel=None, rules_channel: discord.TextChannel=None, gifts_channel: discord.TextChannel=None):
  if interaction.guild.name in SERVER_NAMES:
    await interaction.response.send_message("This server is already setup in the bot you don't need to do it again.", ephemeral=True)
  else:  
    server = interaction.guild

    server_name = server.name  # Get the server name
    server_id = server.id

    SERVER_NAMES.append(server_name)
    with open('./StuffForKeeping/server_names.txt', 'a') as server_names_file:
      server_names_file.write(f"\n{server_name}")
      server_names_file.close()
    
    
    SERVER_IDS.append(server_id)
    with open('./StuffForKeeping/server_ids.txt', 'a') as server_ids_file:
      server_ids_file.write(f"\n{server_id}")
      server_ids_file.close()
      
    
    REACTION_ROLES_CHANNEL.append(server_name)
    REACTION_ROLES_CHANNEL.append(reaction_roles.id)
    with open('./StuffForKeeping/roles_channel.txt', 'a') as roles_channel_file:
      roles_channel_file.write(f"\n{server_name}")
      roles_channel_file.write(f"\n{reaction_roles.id}")
      roles_channel_file.close()


    COUNTDOWN_CHANNEL.append(server_name)
    COUNTDOWN_CHANNEL.append(countdown_channel.id)
    with open('./StuffForKeeping/countdown_channel.txt', 'a') as countdown_channel_file:
      countdown_channel_file.write(f"\n{server_name}")
      countdown_channel_file.write(f"\n{countdown_channel.id}")
      countdown_channel_file.close()
      
      
    WELCOME_CHANNEL.append(server_name)
    WELCOME_CHANNEL.append(welcome_channel.id)
    with open('./StuffForKeeping/welcome_channel.txt', 'a') as welcome_channel_file:
      welcome_channel_file.write(f"\n{server_name}")
      welcome_channel_file.write(f"\n{welcome_channel.id}")
      welcome_channel_file.close()
    
    
    if personal_messages != None:
      PERSONAL_MESSAGES_CATEGORY.append(server_name)
      PERSONAL_MESSAGES_CATEGORY.append(personal_messages.name)
      with open('./StuffForKeeping/personal_messages_cat.txt', 'a') as personal_messages_cat_file:
        personal_messages_cat_file.write(f"\n{server_name}")
        personal_messages_cat_file.write(f"\n{personal_messages.name}")
        personal_messages_cat_file.close()


    if rules_channel != None:
      RULES_CHANNEL.append(server_name)
      RULES_CHANNEL.append(rules_channel.id)
      with open('./StuffForKeeping/rules_channel.txt', 'a') as rules_channel_file:
        rules_channel_file.write(f"\n{server_name}")
        rules_channel_file.write(f"\n{rules_channel.id}")
        rules_channel_file.close()
      
    
    BIRTHDAY_ROLE.append(server_name)
    BIRTHDAY_ROLE.append(birthday_role.name)
    with open('./StuffForKeeping/birthday_role.txt', 'a') as birthday_role_file:
      birthday_role_file.write(f"\n{server_name}")
      birthday_role_file.write(f"\n{birthday_role.name}")
      birthday_role_file.close()


    CARD_CHANNEL.append(server_name)
    CARD_CHANNEL.append(card_channel.id)
    with open('./StuffForKeeping/card_channel.txt', 'a') as card_channel_file:
      card_channel_file.write(f"\n{server_name}")
      card_channel_file.write(f"\n{card_channel.id}")
      card_channel_file.close()
      
    
    WISHES_CHANNEL.append(server_name)
    WISHES_CHANNEL.append(wishes_channel.id)
    with open('./StuffForKeeping/wishes_channel.txt', 'a') as wishes_channel_file:
      wishes_channel_file.write(f"\n{server_name}")
      wishes_channel_file.write(f"\n{wishes_channel.id}")
      wishes_channel_file.close()
      
    
    if gifts_channel != None:
      GIFTS_CHANNEL.append(server_name)
      GIFTS_CHANNEL.append(gifts_channel.id)
      with open('./StuffForKeeping/gifts_channel.txt', 'a') as gifts_channel_file:
        gifts_channel_file.write(f"\n{server_name}")
        gifts_channel_file.write(f"\n{gifts_channel.id}")
        gifts_channel_file.close()
      
    
    MEMORIES_CHANNEL.append(server_name)
    MEMORIES_CHANNEL.append(memories_channel.id)
    with open('./StuffForKeeping/memories_channel.txt', 'a') as memories_channel_file:
      memories_channel_file.write(f"\n{server_name}")
      memories_channel_file.write(f"\n{memories_channel.id}")
      memories_channel_file.close()
      
    ANNOUNCEMENT_CHANNEL.append(server_name)
    ANNOUNCEMENT_CHANNEL.append(announcement_channel.id)  
    with open('./StuffForKeeping/announcement_channel.txt', 'a') as announcement_channel_file:
      announcement_channel_file.write(f"\n{server_name}")
      announcement_channel_file.write(f"\n{announcement_channel.id}")
      announcement_channel_file.close()
    
    COUNTDOWN_ROLE.append(server_name)
    COUNTDOWN_ROLE.append(countdown_role.name)
    with open('./StuffForKeeping/coutdown_role.txt', 'a') as coutdown_role_file:
      coutdown_role_file.write(f"\n{server_name}")
      coutdown_role_file.write(f"\n{countdown_role.name}")
      coutdown_role_file.close()
    
    
    
    await interaction.response.send_message(f"You have now setup the bot", ephemeral=True)
    await bot.tree.sync()

@bot.tree.command(name="setup_roles", description = "Setup the reaction roles")
@app_commands.describe(roles="How many roles are there?")
@app_commands.default_permissions(manage_messages=True)
@app_commands.guild_only()
async def setup_roles(interaction: discord.Interaction, roles: int):
  if not interaction.guild.name in SERVER_NAMES:
    await interaction.response.send_message("This server is not in my system yet. Please fix that before you run this command!", ephemeral=True)
  else:
    await interaction.response.send_message("We will now create the reaction roles. Pay attention to the messages below this!!", ephemeral=True)
    server = interaction.guild
    server_name = server.name
    command_channel_id = interaction.channel_id
    main_channel = bot.get_channel(command_channel_id)
    roles_channels = REACTION_ROLES_CHANNEL[REACTION_ROLES_CHANNEL.index(server_name) + 1]
    roles_channel = await bot.fetch_channel(roles_channels)
    reaction_roles = []
    emojis = []
    role_names = []
    foundNameAlready = False
    values = []
    embed_title = ""
    count = 0
    addWhatIsRoleFor = ""
    
    def check(response_message):
      return response_message.author == interaction.user and response_message.channel == interaction.channel
    
    await main_channel.send("What is these reaction roles for?")

    user_response = await bot.wait_for('message', check=check, timeout=60)
    if user_response:
      embed_title = user_response.content
      count = count + 2
    else:
      await main_channel.send("I didn't receive a response. Exiting the poll setup.")
      count = count + 1
      return
    
    await main_channel.send("Do you want/need to add what the roles are for?(Yes or No)")

    user_response = await bot.wait_for('message', check=check, timeout=60)
    if user_response:
      addWhatIsRoleFor = user_response.content.lower()
      count = count + 2
    else:
      await main_channel.send("I didn't receive a response. Exiting the poll setup.")
      count = count + 1
      return

    for i in range(roles):
      await main_channel.send(f"What is the emoji for role {i+1}?")

      user_response = await bot.wait_for('message', check=check, timeout=60)
      if user_response:
        reaction_roles.append(user_response.content)
        emojis.append(user_response.content)
        count = count + 2
      else:
        await main_channel.send("I didn't receive a response. Exiting the poll setup.")
        count = count + 1
        return
        
      await main_channel.send(f"What is the the role name for that emoji that you just gave me?")

      user_response = await bot.wait_for('message', check=check, timeout=60)
      if user_response:
        reaction_roles.append(user_response.content)
        role_names.append(user_response.content)
        count = count + 2
      else:
        await main_channel.send("I didn't receive a response. Exiting the poll setup.")
        count = count + 1
        return
      if "y" in addWhatIsRoleFor.lower() : 
        await main_channel.send(f"What is this role for?")

        user_response = await bot.wait_for('message', check=check, timeout=60)
        if user_response:
          values.append(user_response.content)
          count = count + 2
        else:
          await main_channel.send("I didn't receive a response. Exiting the poll setup.")
          count = count + 1
          return

    await main_channel.purge(limit=count)

    
    for role_for in REACTION_ROLES:  # Iterate directly through REACTION_ROLES
      if role_for[0] == server_name:  # Check only the first element of each inner list
        foundNameAlready = True
        serverindex = REACTION_ROLES.index(role_for)
        break
      else:
        foundNameAlready = False

    if foundNameAlready: 
      for role in reaction_roles:
        REACTION_ROLES[serverindex].append(role)
    else:
      reaction_roles.insert(0, server_name)
      REACTION_ROLES.append(reaction_roles)
      
      
    with open(f'./StuffForKeeping/reactionroles/{server_name}_reaction_roles.txt', 'a') as reaction_roles_file:
      for role in reaction_roles:
        reaction_roles_file.write(f"{role}\n")
      reaction_roles_file.close()
    
    embed = discord.Embed(title=embed_title, description="Get your roles here!")
    if "y" in addWhatIsRoleFor.lower() : 
      for i in range(roles):
        embed.add_field(name=f"{emojis[i]} {role_names[i]}", value=f"{values[i]}", inline=False)
    else: 
      for i in range(roles):
        embed.add_field(name=f"{emojis[i]} {role_names[i]}", value="", inline=False)
    rolesmessage = await roles_channel.send(embed=embed)
    for emoji in emojis:
      await rolesmessage.add_reaction(f'{emoji}')

@bot.event
async def on_raw_reaction_add(payload):
  server = bot.get_guild(payload.guild_id)  # Fetch the server object
  server_name = server.name  # Get the server name directly
  reaction = payload.emoji  # Get the emoji object
  user = payload.member  # Get the member object who reacted
  channel = await bot.fetch_channel(payload.channel_id)  # Get the channel object

  # Find the reaction roles channel for this server
  reaction_roles_channel = None
  for channel_id in REACTION_ROLES_CHANNEL:
    if channel_id in SERVER_NAMES:
      continue
    if int(channel_id) == channel.id: # Check if channel ID matches server ID
      reaction_roles_channel = await bot.fetch_channel(channel_id)
      break  # Exit loop after finding a match

  if not reaction_roles_channel:
    print(f"Couldn't find reaction roles channel for server: {server.name}")
    return  # Exit if no reaction roles channel found

  # Check if reaction happened in the designated reaction role channel and for the correct server
  if payload.channel_id != reaction_roles_channel.id or server.id != payload.guild_id:
    print("This is failing")
    return

  # Ignore reactions from the bot itself
  if user.bot:
    print("They are a bot")
    return

  # Build the list of reaction roles for this server
  reaction_roles_local = []
  for roles in REACTION_ROLES:
    if roles[0] == server_name:
      reaction_roles_local.extend(roles[1:])  # Add all elements from index 1 onwards
      break  # Exit loop after finding a match

  # Check if the emoji matches a configured reaction role
  if f'{reaction}' in reaction_roles_local:
    role_name = reaction_roles_local[reaction_roles_local.index(f'{reaction}') + 1]

    # Check if role_name is not None before assigning
    if role_name:
      role = discord.utils.get(user.guild.roles, name=role_name)
      if role:
        try:
          await user.add_roles(role)
          print(f"Assigned role '{role.name}' to {user.name}")
        except discord.HTTPException as e:
          print(f"Error assigning role: {e}")
      else:
        print(f"Role '{role_name}' not found on the server.")



@bot.event
async def on_raw_reaction_remove(payload):
  user_id = payload.user_id
  guild_id = payload.guild_id
  server = bot.get_guild(payload.guild_id)  # Fetch the server object
  server_name = server.name  # Get the server name directly
  reaction = payload.emoji  # Get the emoji object
  user = payload.member  # Get the member object who reacted
  channel = await bot.fetch_channel(payload.channel_id)  # Get the channel object

  reaction_roles_channel = None
  for channel_id in REACTION_ROLES_CHANNEL:
    if channel_id in SERVER_NAMES:
      continue
    if int(channel_id) == channel.id: # Check if channel ID matches server ID
      reaction_roles_channel = await bot.fetch_channel(channel_id)
      break  # Exit loop after finding a match



  if payload.channel_id != reaction_roles_channel.id or server.id != payload.guild_id:
    print("This is failing")
    return
  
  guild = bot.get_guild(guild_id)  # Fetch the guild object
  user = guild.get_member(user_id)  # Get the member object  

  # Ignore reactions from the bot itself
  if user.bot:
    print("They are a bot")
    return


  reaction_roles_local = []
  for roles in REACTION_ROLES:
    if roles[0] == server_name:
      reaction_roles_local.extend(roles[1:])  # Add all elements from index 1 onwards
      break  # Exit loop after finding a match

  # Check if the emoji matches a configured reaction role
  if f'{reaction}' in reaction_roles_local:
    role_name = reaction_roles_local[reaction_roles_local.index(f'{reaction}') + 1]
    
    # Check if role_name is not None before assigning
    if role_name:
      role = discord.utils.get(user.guild.roles, name=role_name)
      if role:
        try:
          await user.remove_roles(role)
          print(f"Removed role '{role.name}' to {user.name}")
        except discord.HTTPException as e:
          print(f"Error removeing role: {e}")
      else:
        print(f"Role '{role_name}' not found on the server.")

@bot.tree.command(name="create_personal_message", description="Create a channel for someone to create a personal message for this person!")
@app_commands.describe(user="Who is the person writing the personal message?")
@app_commands.describe(name="What would you like to name the channel?")
@app_commands.guild_only()
async def create_personal_message(interaction: discord.Interaction, user: discord.Member, name: str):
  if not interaction.guild.name in SERVER_NAMES:
    await interaction.response.send_message("This server is not in my system yet. Please fix that before you run this command!", ephemeral=True)
  elif not interaction.guild.name in PERSONAL_MESSAGES_CATEGORY:
    await interaction.response.send_message("This server dosen't have a peronal messages category or alteast that I see, sorry. :(", ephemeral=True)
  else:
    guild = interaction.guild
    await interaction.response.send_message("I will now create that channel!", ephemeral=True)
    role_name = None
    category_name = None
    for role in BIRTHDAY_ROLE:
      if role == guild.name:
        role_name = BIRTHDAY_ROLE[BIRTHDAY_ROLE.index(role) + 1]
    for category in PERSONAL_MESSAGES_CATEGORY:
      if category == guild.name:
        category_name = PERSONAL_MESSAGES_CATEGORY[PERSONAL_MESSAGES_CATEGORY.index(category) + 1]
    categoryPersMess = discord.utils.get(guild.categories, name=category_name)
    birthday_role = discord.utils.get(guild.roles, name=role_name)
    overwrites = {
      guild.default_role: discord.PermissionOverwrite(send_messages=False, read_message_history=False),
      birthday_role: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True),
      user: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True)
    }

    await guild.create_text_channel(name, category=categoryPersMess, overwrites=overwrites)

@bot.event
async def on_member_join(member):
  serverName = member.guild.name
  welcome_channel_id = 0
  countdown_channel_id = 0
  reaction_roles_channel_id = 0
  rules_channel_id = 0
  rules_channel_found = False
  card_channel_id = 0
  wishes_channel_id = 0
  gifts_channel_id = 0
  gifts_channel_found = False
  memories_channel_id = 0
  index = 0
  for Welcome_channel in WELCOME_CHANNEL:
    if Welcome_channel == serverName:
      index = WELCOME_CHANNEL.index(Welcome_channel)
      welcome_channel_id = WELCOME_CHANNEL[index+1]
    else:
      continue

  for countdown_channel in COUNTDOWN_CHANNEL:
    if countdown_channel == serverName:
      index = COUNTDOWN_CHANNEL.index(countdown_channel)
      countdown_channel_id = COUNTDOWN_CHANNEL[index+1]
    else:
      continue

  for roles_channel in REACTION_ROLES_CHANNEL:
    if roles_channel == serverName:
      index = REACTION_ROLES_CHANNEL.index(roles_channel)
      reaction_roles_channel_id = REACTION_ROLES_CHANNEL[index+1]
    else:
      continue

  for rules_channel in RULES_CHANNEL:
    if rules_channel == serverName:
      index = RULES_CHANNEL.index(rules_channel)
      rules_channel_id = RULES_CHANNEL[index+1]
      rules_channel_found = True
    else:
      continue

  for card_channel in CARD_CHANNEL:
    if card_channel == serverName:
      index = CARD_CHANNEL.index(card_channel)
      card_channel_id = CARD_CHANNEL[index+1]
    else:
      continue

  for wishes_channel in WISHES_CHANNEL:
    if wishes_channel == serverName:
      index = CARD_CHANNEL.index(wishes_channel)
      wishes_channel_id = WISHES_CHANNEL[index+1]
    else:
      continue

  for gifts_channel in GIFTS_CHANNEL:
    if gifts_channel == serverName:
      index = GIFTS_CHANNEL.index(gifts_channel)
      gifts_channel_id = WISHES_CHANNEL[index+1]
      gifts_channel_found = True
    else:
      continue

  for memories_channel in MEMORIES_CHANNEL:
    if memories_channel == serverName:
      index = MEMORIES_CHANNEL.index(memories_channel)
      memories_channel_id = MEMORIES_CHANNEL[index+1]
    else:
      continue
  
  channel = bot.get_channel(welcome_channel_id)
  embed = discord.Embed(title="Welcome New User!!!!", description=f"Welcome to the {serverName} discord server <@!{member.id}>!!")
  embed.add_field(name="Please read what is below!!", value="", inline=False)
  embed.add_field(name=f"Get your roles in: <#{reaction_roles_channel_id}>!", value="", inline=False)
  embed.add_field(name=f"View the countdown here: <#{countdown_channel_id}>!", value="", inline=False)
  if rules_channel_found:
    embed.add_field(name=f"Read the rules here: <#{rules_channel_id}>!", value="", inline=False)
  embed.add_field(name=f"Sign the card here: <#{card_channel_id}>!", value="", inline=False)
  embed.add_field(name=f"Send your wishes here: <#{wishes_channel_id}>!", value="", inline=False)
  if gifts_channel_found:
    embed.add_field(name=f"Give some gifts here: <#{gifts_channel_id}>!", value="", inline=False)
  embed.add_field(name=f"Share your memories here: <#{memories_channel_id}>!", value="", inline=False)
  await channel.send(member.mention, embed=embed)

async def is_owner_or_respond(interaction: discord.Interaction):
  if not interaction.user.id == 798267958270099557:
    # Inform user they lack permission
    await interaction.response.send_message("This command is for the bot owner only!", ephemeral=True)
    raise discord.app_commands.CommandError  # Raise an error to stop further execution
  return True


@bot.tree.command(name="send_announcement", description="Send an announcemet for all the announcements channels for all the servers!")
@app_commands.describe(mention_everyone="Do you want to ping everyone?")
@app_commands.default_permissions(administrator=True)
@app_commands.check(is_owner_or_respond)
@app_commands.guild_only()
@app_commands.choices(mention_everyone=[
  discord.app_commands.Choice(name="Yes", value=1),
  discord.app_commands.Choice(name="No", value=2)
])
async def send_announcement(interaction: discord.Interaction, mention_everyone: discord.app_commands.Choice[int]):
  await interaction.response.send_message("I will now do that!", ephemeral=True)
  guild = interaction.guild
  guild.default_role
  channel = interaction.channel_id
  user = interaction.user
  message = None
  main_channel = await bot.fetch_channel(channel)
  await main_channel.send(f"What is the message?")
  def check(response_message):
    return response_message.author == interaction.user and response_message.channel == interaction.channel
  try:
    user_response = await bot.wait_for('message', check=check, timeout=10)
  except TimeoutError:
    user_response = None
  if user_response != None:
    message = user_response.content
    await main_channel.purge(limit=2)
  else:
    await user.send("I didn't receive a response. Exiting the message announcement")
    await main_channel.purge(limit=1)
    
  if message != None:
    announcement_channels_local = []
    servers = []
    for channels in ANNOUNCEMENT_CHANNEL:
      if channels in SERVER_NAMES:
        continue
      else:
        announcement_channels_local.append(int(channels))
    for id in SERVER_IDS:
      server = await bot.fetch_guild(int(id))
      servers.append(server)
    for ids in announcement_channels_local:
      channel = await bot.fetch_channel(ids)
      this_server = servers[announcement_channels_local.index(ids)]
      if mention_everyone.name == "Yes":
        await channel.send(f"{message} \n {this_server.default_role}")
      else:
        await channel.send(message)

@bot.tree.command(name="countdown", description="Start the countdown for a specific number of days")
@app_commands.describe(days="How many days until the event?")
@app_commands.default_permissions(administrator=True)  # Replace with appropriate permission
@app_commands.guild_only()
async def countdown(interaction: discord.Interaction, days: int):
  if not interaction.guild.name in SERVER_NAMES:
    await interaction.response.send_message("This server is not in my system yet. Please fix that before you run this command!", ephemeral=True)
  elif interaction.guild.name in COUNTDOWNS:
    await interaction.response.send_message("This server has already had the coutdown setup, you don't need to do it again!")
  else:
    correct = False
    channel = interaction.channel
    days_until_birthday = days
    count = 0
    await interaction.response.send_message("Ok, we will setup the coutdown!", ephemeral=True)
    while not correct:
      date = get_date(days_until_birthday)
      await channel.send(f"Is this date their birthday? {date}")
      def check(response_message):
        return response_message.author == interaction.user and response_message.channel == interaction.channel

      user_response = await bot.wait_for('message', check=check, timeout=60)
      if user_response:
        count = count + 2
      else:
        return
      if "y" in user_response.content.lower():
        correct = True
      else:
        await channel.send("You said it wasen't correct so please give the actual number of days until their birthday!")
        user_response = await bot.wait_for('message', check=check, timeout=60)
        if user_response:
          count = count + 2
          days_until_birthday = int(user_response.content)
        else:
          return
    days_until_birthday = days_until_birthday - 1
    await channel.purge(limit=count)
    COUNTDOWNS.append(interaction.guild.name)
    COUNTDOWNS.append(str(days_until_birthday))
    with open('./StuffForKeeping/coutdowns.txt', 'a') as countdowns_file:
      countdowns_file.write(f"\n{interaction.guild.name}")
      countdowns_file.write(f"\n{str(days_until_birthday)}")
      countdowns_file.close()
      
@bot.tree.command(name="remove_server", description="Remove the server from the bot when you are done.")
@app_commands.default_permissions(administrator=True)  # Replace with appropriate permission
@app_commands.guild_only()
async def remove_server(interaction: discord.Interaction):
  if not interaction.guild.name in SERVER_NAMES:
    await interaction.response.send_message("This server is not in my system yet. You can't run this command yet!", ephemeral=True)
  else:
    await interaction.response.send_message("I will now remove the stuff related to this server from the bot.", ephemeral=True)
    try:
      SERVER_NAMES.pop(SERVER_NAMES.index(interaction.guild.name))
    except ValueError:
      pass
    try:
      SERVER_IDS.pop(SERVER_IDS.index(str(interaction.guild.id)))
    except ValueError:
      pass
    try:
      os.remove(f'./StuffForKeeping/reactionroles/{interaction.guild.name}_reaction_roles.txt')
    except FileNotFoundError:
      pass
    try:
      index = ANNOUNCEMENT_CHANNEL.index(interaction.guild.name)
      ANNOUNCEMENT_CHANNEL.pop(index)
      ANNOUNCEMENT_CHANNEL.pop(index)
    except ValueError:
      pass
    try:
      index = BIRTHDAY_ROLE.index(interaction.guild.name)
      BIRTHDAY_ROLE.pop(index)
      BIRTHDAY_ROLE.pop(index)
    except ValueError:
      pass
    try:
      index = CARD_CHANNEL.index(interaction.guild.name)
      CARD_CHANNEL.pop(index)
      CARD_CHANNEL.pop(index)
    except ValueError:
      pass
    try:
      index = COUNTDOWN_CHANNEL.index(interaction.guild.name)
      COUNTDOWN_CHANNEL.pop(index)
      COUNTDOWN_CHANNEL.pop(index)
    except ValueError:
      pass
    try:
      index = COUNTDOWN_ROLE.index(interaction.guild.name)
      COUNTDOWN_ROLE.pop(index)
      COUNTDOWN_ROLE.pop(index)
    except ValueError:
      pass
    try:
      index = COUNTDOWNS.index(interaction.guild.name)
      COUNTDOWNS.pop(index)
      COUNTDOWNS.pop(index)
    except ValueError:
      pass
    try:
      index = GIFTS_CHANNEL.index(interaction.guild.name)
      GIFTS_CHANNEL.pop(index)
      GIFTS_CHANNEL.pop(index)
    except ValueError:
      pass
    try:
      index = MEMORIES_CHANNEL.index(interaction.guild.name)
      MEMORIES_CHANNEL.pop(index)
      MEMORIES_CHANNEL.pop(index)
    except ValueError:
      pass
    try:
      index =  REACTION_ROLES_CHANNEL.index(interaction.guild.name)
      REACTION_ROLES_CHANNEL.pop(index)
      REACTION_ROLES_CHANNEL.pop(index)
    except ValueError:
      pass
    try:
      index = RULES_CHANNEL.index(interaction.guild.name)
      RULES_CHANNEL.pop(index)
      RULES_CHANNEL.pop(index)
    except ValueError:
      pass
    try:
      index = WELCOME_CHANNEL.index(interaction.guild.name)
      WELCOME_CHANNEL.pop(index)
      WELCOME_CHANNEL.pop(index)
    except ValueError:
      pass
    try:
      index = WISHES_CHANNEL.index(interaction.guild.name)
      WISHES_CHANNEL.pop(index)
      WISHES_CHANNEL.pop(index)
    except ValueError:
      pass
    try:
      index = PERSONAL_MESSAGES_CATEGORY.index(interaction.guild.name)
      PERSONAL_MESSAGES_CATEGORY.pop(index)
      PERSONAL_MESSAGES_CATEGORY.pop(index)
    except ValueError:
      pass
    for roles in REACTION_ROLES:
      if roles[0] == interaction.guild.name:
        REACTION_ROLES.remove(roles)
    
    
    
    with open('./StuffForKeeping/announcement_channel.txt','w') as announcement_channel_file:
      if len(ANNOUNCEMENT_CHANNEL) == 0:
        pass
      else:
        for achannel in ANNOUNCEMENT_CHANNEL:
          announcement_channel_file.write(f"\n{achannel}")
      announcement_channel_file.close()
      
    with open('./StuffForKeeping/birthday_role.txt','w') as birthday_role_file:
      if len(BIRTHDAY_ROLE) == 0:
        pass
      else:
        for Brole in BIRTHDAY_ROLE:
          birthday_role_file.write(f"\n{Brole}")
      birthday_role_file.close()
      
    with open('./StuffForKeeping/card_channel.txt','w') as card_channel_file:
      if len(CARD_CHANNEL) == 0:
        pass
      else:
        for cchannel in CARD_CHANNEL:
          card_channel_file.write(f"\n{cchannel}")
      card_channel_file.close()
    
    with open('./StuffForKeeping/countdown_channel.txt','w') as countdown_channel_file:
      if len(COUNTDOWN_CHANNEL) == 0:
        pass
      else:
        for cdchannel in COUNTDOWN_CHANNEL:
          countdown_channel_file.write(f"\n{cdchannel}")
      countdown_channel_file.close()
      
    with open('./StuffForKeeping/coutdown_role.txt','w') as coutdown_role_file:
      if len(COUNTDOWN_ROLE) == 0:
        pass
      else:
        for cdRole in COUNTDOWN_ROLE:
          coutdown_role_file.write(f"\n{cdRole}")
      coutdown_role_file.close()
      
    with open('./StuffForKeeping/coutdowns.txt','w') as coutdowns_file:
      if len(COUNTDOWNS) == 0:
        pass
      else:
        for coutdown in COUNTDOWNS:
          coutdowns_file.write(f"\n{coutdown}")
      coutdowns_file.close()
      
    with open('./StuffForKeeping/gifts_channel.txt','w') as gifts_channel_file:
      if len(GIFTS_CHANNEL) == 0:
        pass
      else:
        for ghannel in GIFTS_CHANNEL:
          gifts_channel_file.write(f"\n{ghannel}")
      gifts_channel_file.close()
    
    with open('./StuffForKeeping/memories_channel.txt','w') as memories_channel_file:
      if len(MEMORIES_CHANNEL) == 0:
        pass
      else:
        for mchannel in MEMORIES_CHANNEL:
          memories_channel_file.write(f"\n{mchannel}")
      memories_channel_file.close()
      
    with open('./StuffForKeeping/personal_messages_cat.txt','w') as personal_messages_cat_file:
      if len(PERSONAL_MESSAGES_CATEGORY) == 0:
        pass
      else:
        for category in PERSONAL_MESSAGES_CATEGORY:
          personal_messages_cat_file.write(f"\n{category}")
      personal_messages_cat_file.close()
      
    with open('./StuffForKeeping/roles_channel.txt','w') as roles_channel_file:
      if len(REACTION_ROLES_CHANNEL) == 0:
        pass
      else:
        for rchannel in REACTION_ROLES_CHANNEL:
          roles_channel_file.write(f"\n{rchannel}")
      roles_channel_file.close()
      
    with open('./StuffForKeeping/rules_channel.txt','w') as rules_channel_file:
      if len(RULES_CHANNEL) == 0:
        pass
      else:
        for ruchannel in RULES_CHANNEL:
          rules_channel_file.write(f"\n{ruchannel}")
      rules_channel_file.close()
    
    with open('./StuffForKeeping/server_ids.txt','w') as server_ids_file:
      if len(SERVER_IDS) == 0:
        pass
      else:
        for ids in SERVER_IDS:
          server_ids_file.write(f"\n{ids}")
      server_ids_file.close()
    
    with open('./StuffForKeeping/server_names.txt','w') as server_names_file:
      if len(SERVER_NAMES) == 0:
        pass
      else:
        for name in SERVER_NAMES:
          server_names_file.write(f"\n{name}")
      server_names_file.close()
      
    with open('./StuffForKeeping/welcome_channel.txt','w') as welcome_channel_file:
      if len(WELCOME_CHANNEL) == 0:
        pass
      else:
        for wchannel in WELCOME_CHANNEL:
          welcome_channel_file.write(f"\n{wchannel}")
      welcome_channel_file.close()
    
    with open('./StuffForKeeping/wishes_channel.txt','w') as wishes_channel_file:
      if len(WISHES_CHANNEL) == 0:
        pass
      else:
        for wichannel in WISHES_CHANNEL:
          wishes_channel_file.write(f"\n{wichannel}")
      wishes_channel_file.close()
    

      
@tasks.loop(time=midnight)
async def countdown():
  for server in SERVER_NAMES:
    if server in COUNTDOWN_CHANNEL and server in COUNTDOWNS:
      guild = await bot.fetch_guild(SERVER_IDS[SERVER_NAMES.index(server)])
      countdown_channel_id = COUNTDOWN_CHANNEL[COUNTDOWN_CHANNEL.index(server) + 1]
      countdown_role_name = COUNTDOWN_ROLE[COUNTDOWN_ROLE.index(server) + 1]
      countdown_channel = await bot.fetch_channel(countdown_channel_id)
      countdown_role = discord.utils.get(guild.roles, name=countdown_role_name)
      index = COUNTDOWNS.index(server) + 1
      countdown_days = COUNTDOWNS[index]
      if int(countdown_days) == 1:
        await countdown_channel.send(f"{countdown_days} day untill their birthday!!! \n {countdown_role.mention}")
      elif int(countdown_days) == 0:
        await countdown_channel.send(f"Today is their birthday!!!!!!!!!!!!!!!! \n {countdown_role.mention}")
        announcement_channel = await bot.fetch_channel(int(ANNOUNCEMENT_CHANNEL[ANNOUNCEMENT_CHANNEL.index(server) + 1]))
        await announcement_channel.send("For the server owners. Make sure to run /remove_server when you are done, and before you deleate the server.")
        COUNTDOWNS.pop(index - 1)
        COUNTDOWNS.pop(index - 1)
        continue
      else:
        await countdown_channel.send(f"{countdown_days} days untill their birthday!!! \n {countdown_role.mention}")
      new_coutdown_days = int(countdown_days) - 1
      COUNTDOWNS.pop(index)
      COUNTDOWNS.insert(index, str(new_coutdown_days))
  with open('./StuffForKeeping/coutdowns.txt', 'w') as countdowns_file:
    for index in COUNTDOWNS:
      countdowns_file.write(f"\n{index}")
    countdowns_file.close()
      
      

      
      

bot.run(BOT_TOKEN)