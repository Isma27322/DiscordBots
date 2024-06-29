import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands
import random
import time
import asyncio

def read_bot_token():
  with open('../Tokens/CloudBerryToken.txt', 'r') as file:
    return file.read().strip()
  

BOT_TOKEN = read_bot_token()
WELCOME_CHANNEL_ID = 1240344179112939570
SERVER_ID = 1240143567075410021
REACTION_ROLES_CHANNEL_ID = 1240344902433509479
REACTION_ROLES_EMOJIS = []
REACTION_ROLES_ROLE_NAMES = []
EMPLOYMENT_SEND_TO_CHANNEL = 1241203942080254044
OPEN_APPLICATIONS_USERNAME = []
OPEN_APPLICATIONS_DISCORD_ID = []
OPEN_APPLICATIONS_RANK = []
OPEN_APPLICATIONS_DEPARTMENT = []
MRQUESTIONS = ['1. What is your Roblox username?', '2. What is your Discord username?', 
'3. Why do you want to work at Cloudberry cafe?', '4. What will you do to benefit cloudberry cafe?',
'5. How would you rate your activity on Roblox on a scale of 1 to 10?',
'6. How would you rate your activity on Discord on a scale of 1 to 10?',
'7. What are your previous and current MR+ roles?']
HRQUESTIONS = ['1. What is your Roblox username?',
'2. What is your Discord username?',
'3. Why do you want to work at Cloudberry cafe?',
'4. How will you benefit cloudberry cafe?',
'5. How would you rate your activity on Roblox on a scale of 1 to 10?',
'6. How would you rate your activity on Discord on a scale of 1 to 10?',
'7. What are your previous and current MR+ roles?',
'8. What department are you interested in working in? Public relations or Human Resources?',
'9. What experience do you have in that department or a similar department?']
CLOSED_APPLICATIONS_DISCORD_ID = []
TICKET_CHANNEL_IDS = []

with open('ReactionRolesNames.txt', 'r') as file:
  # Read all lines at once (check if any lines exist)
  lines = file.readlines()
  if not lines:
    print("File is empty.")
  else:
    # Find the first non-empty line (assuming headers are at the beginning)
    start_line = 0
    for line in lines:
      line = line.strip()  # Remove leading/trailing whitespace
      if line:
        has_data = True  # Set flag if any line is found (excluding headers)
        break
      start_line += 1

    # Iterate through lines starting from the first non-empty line
    for line in lines[start_line:]:
      line = line.strip()
      REACTION_ROLES_ROLE_NAMES.append(line)

with open('ReactionRoleEmojis.txt', 'r') as file:
  # Read all lines at once (check if any lines exist)
  lines = file.readlines()
  if not lines:
    print("File is empty.")
  else:
    # Find the first non-empty line (assuming headers are at the beginning)
    start_line = 0
    for line in lines:
      line = line.strip()  # Remove leading/trailing whitespace
      if line:
        has_data = True  # Set flag if any line is found (excluding headers)
        break
      start_line += 1

    # Iterate through lines starting from the first non-empty line
    for line in lines[start_line:]:
      line = line.strip()
      REACTION_ROLES_EMOJIS.append(line)

with open('./Applications/open_applications_department.txt', 'r') as open_applications_department:
  lines = open_applications_department.readlines()
  if len(lines) != 0:
    lines.pop(0)
    for line in lines:
      OPEN_APPLICATIONS_DEPARTMENT.append(line.strip())
  open_applications_department.close()
  
with open('./Applications/open_applications_discord_id.txt', 'r') as open_applications_discord_id:
  lines = open_applications_discord_id.readlines()
  if len(lines) != 0:
    lines.pop(0)
    for line in lines:
      OPEN_APPLICATIONS_DISCORD_ID.append(line.strip())
  open_applications_discord_id.close()

with open('./Applications/open_applications_rank.txt', 'r') as open_applications_rank:
  lines = open_applications_rank.readlines()
  if len(lines) != 0:
    lines.pop(0)
    for line in lines:
      OPEN_APPLICATIONS_RANK.append(line.strip())
  open_applications_rank.close()

with open('./Applications/open_applications_username.txt', 'r') as open_applications_username:
  lines = open_applications_username.readlines()
  if len(lines) != 0:
    lines.pop(0)
    for line in lines:
      OPEN_APPLICATIONS_USERNAME.append(line.strip())
  open_applications_username.close()
  
with open('./Applications/closed_applications_discord_id.txt', 'r') as closed_applications_discord_id:
  lines = closed_applications_discord_id.readlines()
  if len(lines) != 0:
    lines.pop(0)
    for line in lines:
      CLOSED_APPLICATIONS_DISCORD_ID.append(line.strip())
  closed_applications_discord_id.close()
  
with open('./ticket_numbers/open_tickets_channel_ids.txt', 'r') as open_tickets:
  lines = open_tickets.readlines()
  if len(lines) != 0:
    lines.pop(0)
    for line in lines:
      TICKET_CHANNEL_IDS.append(int(line.strip()))
  open_tickets.close()

def write_to_files():
  with open('./Applications/open_applications_department.txt', 'w') as open_applications_department:
    for department in OPEN_APPLICATIONS_DEPARTMENT:
      open_applications_department.write(f"\n{department}")
    open_applications_department.close()
  
  with open('./Applications/open_applications_discord_id.txt', 'w') as open_applications_discord_id:
    for id in OPEN_APPLICATIONS_DISCORD_ID:
      open_applications_discord_id.write(f"\n{id}")
    open_applications_discord_id.close()
  
  with open('./Applications/open_applications_rank.txt', 'w') as open_applications_rank:
    for rank in OPEN_APPLICATIONS_RANK:
      open_applications_rank.write(f"\n{rank}")
    open_applications_rank.close()
  
  with open('./Applications/open_applications_username.txt', 'w') as open_applications_username:
    for username in OPEN_APPLICATIONS_USERNAME:
      open_applications_username.write(f"\n{username}")
    open_applications_username.close()

  with open('./Applications/closed_applications_discord_id.txt', 'w') as closed_applications_discord_id:
    for closed_id in CLOSED_APPLICATIONS_DISCORD_ID:
      closed_applications_discord_id.write(f"\n{closed_id}")
    closed_applications_discord_id.close()

def write_ticket_channels():
  with open('./ticket_numbers/open_tickets_channel_ids.txt', 'w') as open_tickets:
    for id in TICKET_CHANNEL_IDS:
      open_tickets.write(f"\n{id}")

def read_ticket_file(type): 
  with open(f'./ticket_numbers/{type}.txt', 'r') as ticket_file_read:
    lines = ticket_file_read.readlines()
    for line in lines:
      number = line.strip()
      return int(number)
    ticket_file_read.close()

def write_ticket_file(type, number): 
  with open(f'./ticket_numbers/{type}.txt', 'w') as ticket_file_write:
    ticket_file_write.write(str(number))
    ticket_file_write.close()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Hello world")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)
    
@bot.event
async def on_message(message):
  if message.channel.id == 1240848125476737185 or message.channel.id == 1240846954854875218 or message.channel.id == 1240706253098061874:
    await message.create_thread(name="Discussion", auto_archive_duration=1440)
    await message.add_reaction("<:checkmark:1240830355984875561>")
    await message.add_reaction("<:xmark:1240830446355353664>")
  if message.channel.id == 1241203942080254044 and message.author != bot.user:
    if "1." in message.content and "2." in message.content and "3." in message.content and "4." in message.content  and "5." in message.content and "6." in message.content:
      await message.add_reaction("<:checkmark:1240830355984875561>")
      await message.add_reaction("<:xmark:1240830446355353664>")

@bot.tree.command(name="reactionroles", description="Setup the reaction roles")
@app_commands.describe(roles="How many roles are there?")
@app_commands.default_permissions(view_audit_log=True)  # Hide the command
@app_commands.guild_only()
async def reactionroles(interaction: discord.Interaction, roles: int):
  await interaction.response.send_message("We will now create the reaction roles. Pay attention to the messages below this!!", ephemeral=True)
  emojis = []
  role_names = []
  command_channel_id = interaction.channel.id
  main_channel = bot.get_channel(command_channel_id)
  reaction_roles_channel = bot.get_channel(REACTION_ROLES_CHANNEL_ID)
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
      emojis.append(user_response.content)
      REACTION_ROLES_EMOJIS.append(user_response.content)
      count = count + 2
    else:
      await main_channel.send("I didn't receive a response. Exiting the poll setup.")
      count = count + 1
      return
    
    await main_channel.send(f"What is the the role name for that emoji that you just gave me?")

    user_response = await bot.wait_for('message', check=check, timeout=60)
    if user_response:
      role_names.append(user_response.content)
      REACTION_ROLES_ROLE_NAMES.append(user_response.content)
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
  
  with open('ReactionRolesNames.txt', 'a') as reactionRolesNames:
    for name in role_names :
      reactionRolesNames.write("\n")
      reactionRolesNames.write(name)
    reactionRolesNames.close()
      
  with open('ReactionRoleEmojis.txt', 'a') as reactionRolesEmojis:
    for emoji in emojis:
      reactionRolesEmojis.write("\n")
      reactionRolesEmojis.write(emoji)
    reactionRolesEmojis.close()

  
  embed = discord.Embed(title=embed_title, description="Get your roles here!")
  if "y" in addWhatIsRoleFor.lower() : 
    for i in range(roles):
      embed.add_field(name=f"{emojis[i]} {role_names[i]}", value=f"{values[i]}", inline=False)
  else: 
    for i in range(roles):
      embed.add_field(name=f"{emojis[i]} {role_names[i]}", value="", inline=False)
      
  rolesmessage = await reaction_roles_channel.send(embed=embed)
  for emoji in emojis:
    await rolesmessage.add_reaction(f'{emoji}')

@bot.event
async def on_raw_reaction_add(payload):
  reaction = payload.emoji  # Get the emoji object
  user = payload.member

  if payload.channel_id != REACTION_ROLES_CHANNEL_ID or payload.guild_id != SERVER_ID:
    return

  # Ignore reactions from the bot itself
  if user.bot:
    return

  # Print the emoji being reacted with and the list for debugging

  # Check if the emoji matches a configured reaction role
  if f'{reaction}' in REACTION_ROLES_EMOJIS:
    role_name = REACTION_ROLES_ROLE_NAMES[REACTION_ROLES_EMOJIS.index(f'{reaction}')]
    
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
  reaction = payload.emoji  # Get the emoji object
  user_id = payload.user_id
  guild_id = payload.guild_id

  if payload.channel_id != REACTION_ROLES_CHANNEL_ID or guild_id != SERVER_ID:
    return
  
  guild = bot.get_guild(guild_id)  # Fetch the guild object
  user = guild.get_member(user_id)  # Get the member object  

  # Ignore reactions from the bot itself
  if user.bot:
    return

  # Print the emoji being reacted with and the list for debugging

  # Check if the emoji matches a configured reaction role
  if f'{reaction}' in REACTION_ROLES_EMOJIS:
    role_name = REACTION_ROLES_ROLE_NAMES[REACTION_ROLES_EMOJIS.index(f'{reaction}')]
    
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
      
@bot.tree.command(name="ban", description="Ban a user from the server")
@app_commands.describe(user="What user would you like to ban?")
@app_commands.describe(reason="What is the reason for the ban?")
@app_commands.default_permissions(manage_messages=True)
@app_commands.guild_only()
async def ban(interaction: discord.Interaction, user: discord.Member, reason: str):
  await interaction.response.send_message(f"I will now ban {user.mention}!", ephemeral=True)
  await user.ban(reason=reason)

@bot.tree.command(name="kick", description="Kick a user from the server")
@app_commands.describe(user="What user would you like to kick?")
@app_commands.describe(reason="What is the reason for the kick?")
@app_commands.default_permissions(manage_messages=True)
@app_commands.guild_only()
async def kick(interaction: discord.Interaction, user: discord.Member, reason: str):
  await interaction.response.send_message(f"I will now kick {user.mention}!", ephemeral=True)
  await user.kick(reason=reason)
    
@bot.event
async def on_member_join(member):
  channel = bot.get_channel(WELCOME_CHANNEL_ID)
  embed = discord.Embed(title="Welcome New User!!!!", description=f"Welcome to the discord server <@!{member.id}>!!")
  embed.add_field(name="Please read what is below!!", value="", inline=False)
  embed.add_field(name=f"Read the rules in: <#1240339086099615854>!", value="", inline=False)
  embed.add_field(name=f"Get your roles in: <#1240344902433509479>!", value="", inline=False)
  embed.add_field(name=f"Verify your account in <#1240369766577868942>!", value="", inline=False)
  embed.add_field(name=f"If you are interesting in working here view this channel! <#1241197261011292170>", value="", inline=False)
  await channel.send(member.mention, embed=embed)

    


@bot.tree.command(name="colorize_roles", description="Colorize the roles")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def colorize_roles(interaction: discord.Interaction):
  guild = interaction.guild
  await interaction.response.send_message("I will now do that!", ephemeral=True)
  default_color = discord.Color.default()  # Get default color object

  roles = guild.roles
  for role in roles:
    if role.color == default_color and role.name != "@everyone":
      new_color = discord.Color(int(f"0x{''.join([str(random.randint(0, 9)) for _ in range(6)])}", 16))  # Generate random hex color
      await role.edit(color=new_color)
      print(f"Assigned color {new_color} to role: {role.name}")
      
      
@bot.tree.command(name="purge_messages", description="Delate messages(Only use when nessarry very dangerous!)")
@app_commands.describe(channel="What channel should I deleate messages in?")
@app_commands.describe(number="How many messages should I deleate?")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def purge_messages(interaction: discord.Interaction, channel: discord.TextChannel, number: int):
  await interaction.response.send_message(f"I will now deleate the messages in <#{channel.id}>", ephemeral=True)
  await channel.purge(limit=number)
  
@bot.tree.command(name="apply", description="Apply for a MR or HR postion at cloudberry cafe!")
@app_commands.describe(rank="What team are you applying for? HR(High rank) or MR(Middle rank?)")
@app_commands.choices(rank=[
  discord.app_commands.Choice(name="MR", value=1),
  discord.app_commands.Choice(name="HR", value=2),
])
@app_commands.default_permissions(administrator=True)
async def apply(interaction: discord.Interaction, rank: discord.app_commands.Choice[int]):
  foundUser = False
  for id in CLOSED_APPLICATIONS_DISCORD_ID:
    if int(id) == interaction.user.id:
      foundUser = True
  if foundUser:
    await interaction.response.send_message("You have already applied. You were either approved or denied. You are not allowed to apply again.")
  else:  
    await interaction.response.send_message(f"""You are now applying for a rank in the {rank.name} team! Please answer the questions I send below!
If you want to exit it at anytime just say "exit"!
There is no time limit for the questions so take your time answering each one!
It is also highly recomended to answer each question with proper grammer to have a higher chance of geting accepted!""")
    channel = interaction.channel
    exitedApplication = False
    employemnt_channel = await bot.fetch_channel(EMPLOYMENT_SEND_TO_CHANNEL)
    fullName = ""
    exitedQuestion = 0
    answers = []
    answers_numbered = []
    if rank.name == "MR":
      fullName = "Middle rank"
      for question in MRQUESTIONS:
        await channel.send(f"Question #{MRQUESTIONS.index(question) + 1}")
        await channel.send(question)
        def check(response_message):
          return response_message.author == interaction.user and response_message.channel == interaction.channel

        user_response = await bot.wait_for('message', check=check)
        if user_response:
          if user_response.content.lower() == "exit":
            await channel.send("Now exiting the application!")
            exitedApplication = True
            exitedQuestion = MRQUESTIONS.index(question) + 1
            break
          else:
            answers.append(user_response.content)
          if MRQUESTIONS.index(question) + 1 == 1:
            OPEN_APPLICATIONS_USERNAME.append(user_response.content)
            OPEN_APPLICATIONS_DISCORD_ID.append(interaction.user.id)
            OPEN_APPLICATIONS_RANK.append(fullName)
            OPEN_APPLICATIONS_DEPARTMENT.append('None')
      answers_numbered.append(f"{fullName} application")      
      for answer in answers:
        answers_numbered.append(f"{MRQUESTIONS[answers.index(answer)]}: \n {answer}") 
    elif rank.name == "HR":
      fullName = "High rank"
      for question in HRQUESTIONS:
        await channel.send(f"Question #{HRQUESTIONS.index(question) + 1}")
        await channel.send(question)
        def check(response_message):
          return response_message.author == interaction.user and response_message.channel == interaction.channel
        
        if HRQUESTIONS.index(question) + 1 == 8:
          public_relations_button = Button(label="Public Relations", style=discord.ButtonStyle.green, custom_id="button1")
          human_resources_button = Button(label="Human Resources", style=discord.ButtonStyle.red, custom_id="button2")

          # Create View to hold buttons
          view = View()
          view.add_item(public_relations_button)
          view.add_item(human_resources_button)

          # Button callback functions
          async def handle_public_relations(interaction: discord.Interaction):
            OPEN_APPLICATIONS_DEPARTMENT.append("Public Relations")
            answers.append("Public Relations")
            # Additional actions based on Public Relations selection (optional)
            await interaction.response.send_message("Public Relations selected!", ephemeral=True)
              

          async def handle_human_resources(interaction: discord.Interaction):
            OPEN_APPLICATIONS_DEPARTMENT.append("Human Resources")
            answers.append("Human Resources")
            # Additional actions based on Human Resources selection (optional)
            await interaction.response.send_message("Human Resources selected!", ephemeral=True)

          # Attach callback functions to buttons
          public_relations_button.callback = handle_public_relations
          human_resources_button.callback = handle_human_resources

          # Send message with the view (containing buttons)
          message = await channel.send(view=view)

          def check(msg):
            return msg.author == bot.user and (msg.content == "Public Relations selected!" or msg.content == "Human Resources selected!")

          try:
            await bot.wait_for('message', check=check)

          except asyncio.TimeoutError:
            # Handle timeout scenario (optional)
            await message.edit(content="Selection timed out!", view=None)  # Remove buttons and display message
          
          continue
        user_response = await bot.wait_for('message', check=check)
        if user_response:
          answers.append(user_response.content)
          if HRQUESTIONS.index(question) + 1 == 8:
            continue
          if user_response.content.lower() == "exit":
            await channel.send("Now exiting the application!")
            exitedApplication = True
            exitedQuestion = HRQUESTIONS.index(question) + 1
            break
          if HRQUESTIONS.index(question) + 1 == 1:
            OPEN_APPLICATIONS_USERNAME.append(user_response.content)
            OPEN_APPLICATIONS_DISCORD_ID.append(interaction.user.id)
            OPEN_APPLICATIONS_RANK.append(fullName)    
      answers_numbered.append(f"{fullName} application")            
      for answer in answers:
        answers_numbered.append(f"{HRQUESTIONS[answers.index(answer)]}: \n {answer}")
    else:
      await channel.send("This isin't working somehow. Please tell the bot owner about this. AKA Isma2732")
      
    if not exitedApplication:
      await channel.send(f"Thank you for showing your interest in working in the {fullName} Team! \n I will forward this to the Human resouce team for them to look over it! \n Then you will get a responce from me within 72 hours with your results!")
      sent_employemnt_message = ""
      for question_answer in answers_numbered:
        sent_employemnt_message = sent_employemnt_message + f"{question_answer}\n"
      employemnt_message = await employemnt_channel.send(sent_employemnt_message)
      await employemnt_message.add_reaction("<:checkmark:1240830355984875561>")
      await employemnt_message.add_reaction("<:xmark:1240830446355353664>")

    else:
      await channel.send("We understand if you don't want to apply quite yet. But you are always welcome to apply in the future if the applications are still open.")
      if fullName == "Middle rank":
        if exitedQuestion > 1:
          OPEN_APPLICATIONS_USERNAME.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
          OPEN_APPLICATIONS_RANK.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
          OPEN_APPLICATIONS_DISCORD_ID.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
      if fullName == "High rank":
        if exitedQuestion > 1:
          if exitedQuestion >= 1 and exitedQuestion < 7:
            OPEN_APPLICATIONS_USERNAME.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
            OPEN_APPLICATIONS_RANK.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
            OPEN_APPLICATIONS_DISCORD_ID.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
          else:
            OPEN_APPLICATIONS_USERNAME.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
            OPEN_APPLICATIONS_RANK.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
            OPEN_APPLICATIONS_DEPARTMENT.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
            OPEN_APPLICATIONS_DISCORD_ID.pop(OPEN_APPLICATIONS_DISCORD_ID.index(interaction.user.id))
            
    write_to_files()
  
  
@bot.tree.command(name="approve_application", description="Approve an application and have me send a dm saying that!")
@app_commands.default_permissions(manage_messages=True)
@app_commands.guild_only()
async def approve_application(interaction: discord.Interaction):
  await interaction.response.send_message("You are now approving an application!", ephemeral=True)
  validUsername = False
  openApplications = ""
  userName = ""
  channel = interaction.channel
  count = 0
  HRApplication = False
  rank = ""
  department = ""
  for applications in OPEN_APPLICATIONS_USERNAME:
    openApplications = openApplications + f"{applications}\n"
    
  while not validUsername:
    
    await channel.send(f"Who are you approving from their roblox username?\n This is my current list of open applications:\n {openApplications}")
    def check(response_message):
      
      return response_message.author == interaction.user and response_message.channel == interaction.channel

    user_response = await bot.wait_for('message', check=check)
    if user_response:
      userName = user_response.content
      count += 2
    
    
    if userName in OPEN_APPLICATIONS_USERNAME:
      validUsername = True
      
    else:
      await channel.send("I can't find that username in my list of open applications! Make sure it is an exact match!")
      count += 1
  
  
  discord_username_id = OPEN_APPLICATIONS_DISCORD_ID[OPEN_APPLICATIONS_USERNAME.index(userName)]
  rank = OPEN_APPLICATIONS_RANK[OPEN_APPLICATIONS_DISCORD_ID.index(discord_username_id)]
  department = OPEN_APPLICATIONS_DEPARTMENT[OPEN_APPLICATIONS_DISCORD_ID.index(discord_username_id)]
  if department != "None":
    HRApplication = True
  await channel.purge(limit=count)
  await channel.send(f"Approved the application for {userName}")
  Application_user = await bot.fetch_user(discord_username_id)
  embed=discord.Embed(title=f"{rank} Application results: cloudberry cafe", color=0x5fe06f)
  embed.add_field(name=f"Greetings {Application_user.display_name}", value="", inline=False)
  embed.add_field(name="The Human resouce department hads reviewed your application!", value="", inline=False)
  embed.add_field(name="And we have decided to approve your application!", value="", inline=False)
  embed.add_field(name=f"Welcome to the {rank} team!", value="", inline=False)
  if HRApplication:
    embed.add_field(name=f"And welcome to the {department} department!", value="", inline=False)
  embed.add_field(name="We are excited to see what you bring!", value="", inline=False)
  embed.add_field(name="", value="", inline=False)
  embed.add_field(name="", value="", inline=False)
  embed.add_field(name="", value="", inline=False)
  embed.add_field(name="Signed,", value="", inline=False)
  embed.add_field(name="Human resource deparment", value="", inline=False)
  await Application_user.send(Application_user.mention, embed=embed)
  
  index = 0
  #find index
  for ids in OPEN_APPLICATIONS_DISCORD_ID:
    if int(ids) == Application_user.id:
      index = OPEN_APPLICATIONS_DISCORD_ID.index(ids)
  
  OPEN_APPLICATIONS_RANK.pop(index)
  OPEN_APPLICATIONS_USERNAME.pop(index)
  OPEN_APPLICATIONS_DEPARTMENT.pop(index)
  OPEN_APPLICATIONS_DISCORD_ID.pop(index)
  CLOSED_APPLICATIONS_DISCORD_ID.append(Application_user.id)
  write_to_files()
  
@bot.tree.command(name="decline_application", description="Approve an application and have me send a dm saying that!")
@app_commands.default_permissions(manage_messages=True)
@app_commands.guild_only()
async def decline_application(interaction: discord.Interaction):
  await interaction.response.send_message("You are now declineing an application!", ephemeral=True)
  validUsername = False
  openApplications = ""
  userName = ""
  channel = interaction.channel
  count = 0
  rank = ""
  for applications in OPEN_APPLICATIONS_USERNAME:
    openApplications = openApplications + f"{applications}\n"
    
  while not validUsername:
    
    await channel.send(f"Who are you declineing from their roblox username?\n This is my current list of open applications:\n {openApplications}")
    def check(response_message):
      
      return response_message.author == interaction.user and response_message.channel == interaction.channel

    user_response = await bot.wait_for('message', check=check)
    if user_response:
      userName = user_response.content
      count += 2
    
    
    if userName in OPEN_APPLICATIONS_USERNAME:
      validUsername = True
      
    else:
      await channel.send("I can't find that username in my list of open applications! Make sure it is an exact match!")
      count += 1
  
  
  discord_username_id = OPEN_APPLICATIONS_DISCORD_ID[OPEN_APPLICATIONS_USERNAME.index(userName)]
  rank = OPEN_APPLICATIONS_RANK[OPEN_APPLICATIONS_DISCORD_ID.index(discord_username_id)]
  await channel.purge(limit=count)
  await channel.send(f"Declined the application for {userName}")
  Application_user = await bot.fetch_user(discord_username_id)
  embed=discord.Embed(title=f"{rank} Application results: cloudberry cafe", color=0xff2222)
  embed.add_field(name=f"Greetings {Application_user.display_name}", value="", inline=False)
  embed.add_field(name="The Human resouce department hads reviewed your application!", value="", inline=False)
  embed.add_field(name="And we have decided to decline your application!", value="", inline=False)
  embed.add_field(name="Please rember to not take this too personally we have many applications we can't approve everyone.", value="", inline=False)
  embed.add_field(name="", value="", inline=False)
  embed.add_field(name="", value="", inline=False)
  embed.add_field(name="", value="", inline=False)
  embed.add_field(name="Signed,", value="", inline=False)
  embed.add_field(name="Human resource deparment", value="", inline=False)
  await Application_user.send(Application_user.mention, embed=embed)
  
  index = 0
  #find index
  for ids in OPEN_APPLICATIONS_DISCORD_ID:
    if int(ids) == Application_user.id:
      index = OPEN_APPLICATIONS_DISCORD_ID.index(ids)
  
  OPEN_APPLICATIONS_RANK.pop(index)
  OPEN_APPLICATIONS_USERNAME.pop(index)
  OPEN_APPLICATIONS_DEPARTMENT.pop(index)
  OPEN_APPLICATIONS_DISCORD_ID.pop(index)
  CLOSED_APPLICATIONS_DISCORD_ID.append(Application_user.id)
  write_to_files()


@bot.tree.command(name="send_message", description="Have me say something in a channel!")
@app_commands.describe(thing_to_say="what should I say?")
@app_commands.describe(channel="where should I send the message?")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def say(interaction: discord.Interaction, thing_to_say: str, channel: discord.TextChannel):
  await interaction.response.send_message("The message is sent", ephemeral=True)
  await channel.send(thing_to_say)

@bot.event
async def on_interaction(interaction: discord.Interaction):
  if interaction.type == discord.InteractionType.component:
    if discord.ComponentType.button:
      if not interaction.user.bot:
        # Check for specific button based on interaction data (e.g., custom_id)
        if interaction.channel.id == 1241171151489601578:
          guild = interaction.guild
          user = interaction.user
          view = View()
          view.add_item(close_ticket)
          if list(interaction.data.values())[0] == "In-Game Support":
            admin_in_game = discord.utils.get(guild.roles, name="In-Game Admin")
            overwrites = {
              guild.default_role: discord.PermissionOverwrite(view_channel=False),
              user: discord.PermissionOverwrite(view_channel=True, send_messages=True
              , create_public_threads=False, create_private_threads=False, read_message_history=True, use_embedded_activities=False
              , send_voice_messages=False, use_application_commands=False),
              admin_in_game: discord.PermissionOverwrite(view_channel=True, send_messages=True
              , create_public_threads=False, create_private_threads=False, read_message_history=True, use_embedded_activities=False
              , send_voice_messages=False, use_application_commands=False),
            }
            supportCategory = discord.utils.get(guild.categories, name="Support")
            ticket_count = read_ticket_file("in_game_support")
            channel = await guild.create_text_channel(f"in-game-support-{ticket_count}", topic="In-Game support ticket", category=supportCategory, overwrites=overwrites)
            write_ticket_file("in_game_support", ticket_count + 1)
            embed = discord.Embed(title="", description="Please state why you are opening the ticket so we can help you better!", color=0x5fe06f)
            await channel.send(f"Greetings <@{user.id}>! Thank you for makeing use of Cloudberry's ticket system! The <@&{admin_in_game.id}> will be in touch soon!", embed=embed, view=view)
            await interaction.response.send_message(f"Ticket created! <#{channel.id}>", ephemeral=True)
            TICKET_CHANNEL_IDS.append(channel.id)
            write_ticket_channels()
            
            
          elif list(interaction.data.values())[0] == "General Questions":
            support_role = discord.utils.get(guild.roles, name="Support Team")
            overwrites = {
              guild.default_role: discord.PermissionOverwrite(view_channel=False),
              user: discord.PermissionOverwrite(view_channel=True, send_messages=True
              , create_public_threads=False, create_private_threads=False, read_message_history=True, use_embedded_activities=False
              , send_voice_messages=False, use_application_commands=False),
              support_role: discord.PermissionOverwrite(view_channel=True, send_messages=True
              , create_public_threads=False, create_private_threads=False, read_message_history=True, use_embedded_activities=False
              , send_voice_messages=False, use_application_commands=False),
            }
            supportCategory = discord.utils.get(guild.categories, name="Support")
            ticket_count = read_ticket_file("general_questions")
            channel = await guild.create_text_channel(f"general_questions-{ticket_count}", topic="In-Game support ticket", category=supportCategory, overwrites=overwrites)
            write_ticket_file("general_questions", ticket_count + 1)
            embed = discord.Embed(title="", description="Please state why you are opening the ticket so we can help you better!", color=0x5fe06f)
            await channel.send(f"Greetings <@{user.id}>! Thank you for makeing use of Cloudberrys ticket system! The <@&{support_role.id}> will be in touch soon!", embed=embed, view=view)
            await interaction.response.send_message(f"Ticket created! <#{channel.id}>", ephemeral=True)
            TICKET_CHANNEL_IDS.append(channel.id)
            write_ticket_channels()
            
            
            
          elif list(interaction.data.values())[0] == "Public relations support":
            public_relations_role = discord.utils.get(guild.roles, name="Public relations")
            overwrites = {
              guild.default_role: discord.PermissionOverwrite(view_channel=False),
              user: discord.PermissionOverwrite(view_channel=True, send_messages=True
              , create_public_threads=False, create_private_threads=False, read_message_history=True, use_embedded_activities=False
              , send_voice_messages=False, use_application_commands=False),
              public_relations_role: discord.PermissionOverwrite(view_channel=True, send_messages=True
              , create_public_threads=False, create_private_threads=False, read_message_history=True, use_embedded_activities=False
              , send_voice_messages=False, use_application_commands=False),
            }
            supportCategory = discord.utils.get(guild.categories, name="Support")
            ticket_count = read_ticket_file("public_relations")
            channel = await guild.create_text_channel(f"public_relations-{ticket_count}", topic="In-Game support ticket", category=supportCategory, overwrites=overwrites)
            write_ticket_file("public_relations", ticket_count + 1)
            embed = discord.Embed(title="", description="Please state why you are opening the ticket so we can help you better!", color=0x5fe06f)
            await channel.send(f"Greetings <@{user.id}>! Thank you for makeing use of Cloudberrys ticket system! The <@&{public_relations_role.id}> department will be in touch soon!", embed=embed, view=view)
            await interaction.response.send_message(f"Ticket created! <#{channel.id}>", ephemeral=True)
            TICKET_CHANNEL_IDS.append(channel.id)
            write_ticket_channels()
            
            
            
            
          elif list(interaction.data.values())[0] == "Human Resources support":
            human_resources_role = discord.utils.get(guild.roles, name="Human resources")
            overwrites = {
              guild.default_role: discord.PermissionOverwrite(view_channel=False),
              user: discord.PermissionOverwrite(view_channel=True, send_messages=True
              , create_public_threads=False, create_private_threads=False, read_message_history=True, use_embedded_activities=False
              , send_voice_messages=False, use_application_commands=False),
              human_resources_role: discord.PermissionOverwrite(view_channel=True, send_messages=True
              , create_public_threads=False, create_private_threads=False, read_message_history=True, use_embedded_activities=False
              , send_voice_messages=False, use_application_commands=False),
            }
            supportCategory = discord.utils.get(guild.categories, name="Support")
            ticket_count = read_ticket_file("human_resources")
            channel = await guild.create_text_channel(f"human_resources-{ticket_count}", topic="In-Game support ticket", category=supportCategory, overwrites=overwrites)
            write_ticket_file("human_resources", ticket_count + 1)
            embed = discord.Embed(title="", description="Please state why you are opening the ticket so we can help you better!", color=0x5fe06f)
            await channel.send(f"Greetings <@{user.id}>! Thank you for makeing use of Cloudberrys ticket system! The <{human_resources_role.id}> will be in touch soon!", embed=embed, view=view)
            await interaction.response.send_message(f"Ticket created! <#{channel.id}>", ephemeral=True)
            TICKET_CHANNEL_IDS.append(channel.id)
            write_ticket_channels()
        if interaction.channel.id in TICKET_CHANNEL_IDS:
          if list(interaction.data.values())[0] == "Close Ticket":
            print("Yes!")
            required_roles = ['Middle rank', 'High rank', 'Senior rank']
            if any(role.name in required_roles for role in interaction.user.roles):
              channel_id = interaction.channel
              messages = [message async for message in channel_id.history()]
              # Add this block after retrieving messages
              non_bot_messages = [message for message in messages if not message.author.bot]
              print(non_bot_messages)
              for message in non_bot_messages:
                print(message.author.display_name)
                print(message.content)
              TICKET_CHANNEL_IDS.pop(TICKET_CHANNEL_IDS.index(interaction.channel.id))
              write_ticket_channels()
              await channel_id.delete()
               
            
            
        
      
  
in_game_support = Button(label="In-Game Support", style=discord.ButtonStyle.green, custom_id="In-Game Support", row=0)
general_question = Button(label="General Questions", style=discord.ButtonStyle.red, custom_id="General Questions", row=0)
public_relations_support = Button(label="Public relations", style=discord.ButtonStyle.blurple, custom_id="Public relations support", row=1)
human_resources_support = Button(label="Human Resources", style=discord.ButtonStyle.gray, custom_id="Human Resources support", row=1)   
close_ticket = Button(label="Close Ticket", style=discord.ButtonStyle.danger, custom_id="Close Ticket", emoji="🔒") 

    
@bot.tree.command(name="setup_tickets", description="Setup the tickets!")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()    
async def setup_tickets(interaction: discord.Interaction, channel: discord.TextChannel):
  embed = discord.Embed(title="Get support!", description="Get Support from our wonderfull comunity!")
  #in_game_support = Button(label="In-Game Support", style=discord.ButtonStyle.gray, custom_id="button1")
  #question = Button(label="Question", style=discord.ButtonStyle.red, custom_id="button2")

  # Create View to hold buttons
  view = View()
  view.add_item(in_game_support)
  view.add_item(general_question)
  view.add_item(public_relations_support)
  view.add_item(human_resources_support)

  # Attach callback functions to buttons
  #in_game_support.callback = handle_in_game_support
  #question.callback = handle_question

  # Send message with the view (containing buttons)
  await channel.send(embed=embed, view=view)
  await interaction.response.send_message("Support tickets setup!", ephemeral=True)
  
"""
#how to edit a message that was already sent  
@bot.tree.command(name="edit_message", description="Edit a message that was sent by the bot!")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def edit_message(interaction: discord.Interaction):
  channel = await bot.fetch_channel(1241197261011292170)
  message = await channel.fetch_message(1243687886356873236)
  await message.edit(content="Greetings @everyone! I appoligize for the ping. But I have exciteing news!! The applications are now open again!! Now to apply you go into my dms(the bots) and run the /apply command with the rank you want to apply for! If you have already applyed you will **not** be allowed to apply again. And make sure to answer all questions and make sure to use grammer for a higher chance of getting accepted.")
  await interaction.response.send_message("Done", ephemeral=True)  

#How to edit embeds that were already sent

@bot.tree.command(name="editembed", description="Edit an embed")
@app_commands.default_permissions(manage_messages=True)
@app_commands.guild_only()
async def editembed(interaction: discord.Interaction):
  channel = bot.get_channel(1240344902433509479)
  message = await channel.fetch_message(1241175106634649660)
  if message.embeds:
    embed = message.embeds[0]  # Assuming there's only one embed
    #embed.remove_field(0) #Remove a field from the embed
    embed.add_field(name="🩷 She / Her", value="", inline=False )
    embed.add_field(name="💙 He / Him", value="", inline=False)
    embed.add_field(name="💚 They / them", value="", inline=False)
    embed.add_field(name="🤍 Ask for pronouns", value="", inline=False)
        

    # Edit the message with the new embed
    await message.edit(embed=embed)
    await interaction.response.send_message("Embed edited successfully!", ephemeral=True)"""


bot.run(BOT_TOKEN)
