import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
import asyncio
import random

def read_bot_token():
  with open('../Tokens/MunchiesCafeToken.txt', 'r') as file:
    return file.read().strip()
  
BOT_TOKEN = read_bot_token()
WELCOME_CHANNEL_ID = 1246348948814434348
SERVER_ID = 1246348948814434345
REACTION_ROLES_CHANNEL_ID = 1246846297588240485
REACTION_ROLES_EMOJIS = []
REACTION_ROLES_ROLE_NAMES = []
EMPLOYMENT_SEND_TO_CHANNEL = 1246843312053289101
OPEN_APPLICATIONS_USERNAME = []
OPEN_APPLICATIONS_DISCORD_ID = []
OPEN_APPLICATIONS_RANK = []
OPEN_APPLICATIONS_DEPARTMENT = []
CLOSED_APPLICATIONS_DISCORD_ID = []
CURRENT_NUMBER = [0]
LAST_AUTHOR = []
MRQUESTIONS = ['1. What is your Roblox username?'
,'2. What is your Discord username?'
,'3. Why do you want to work at Bitebliss Cafe?'
,'4. How can you benefit the cafe?'
,'5. How would you rate your activity on Roblox on a scale of 1 to 10?'
,'6. How would you rate your activity on Discord on a scale of 1 to 10?'
,'7. What are your previous and current MR+ roles?'
,'8. How do you want your results to turn out?']
HRQUESTIONS = ['1. What is your Roblox username?'
,'2. What is your Discord username?'
,'3. Why do you want to work at Bitebliss Cafe?'
,'4. How can you benefit the cafe?'
,'5. How would you rate your activity on Roblox on a scale of 1 to 10?'
,'6. How would you rate your activity on Discord on a scale of 1 to 10?'
,'7. What are your previous and current MR+ roles?'
,'8. How do you want your results to turn out?'
,'9. What department are you interested in working in? Public relations or Human Resources?'
,'10. What experience do you have in that department or a similar department?']
WRONG_NUMBER_RESPONCES = ["I think (user) forgot how to count because the forgot what **(last_number) + 1** was!"
, "I think (user) should lay off the counting for a bit because the forgot what **(last_number) + 1** was!"
, "I think (user) might be counting potatoes instead of numbers."
, "I think a mischievous cat might walked across (user) keyboard? Maybe they should try counting with your fingers next time!"
, "Did (user) forget to carry the one? Maybe they should double-check their counting and try again."
, "Uh oh, seems like someone got a case of the 'number munchies' and forgot what comes after **(last_number)**. Maybe a snack break will help?"
, "Uh oh, seems like (user) got a case of the 'number naps'! Maybe a quick snooze like a red panda will help them remember what comes after **(last_number)**!"
, "Nom nom nom... counting is hard work! Did (user) forget what comes after **(last_number)** because they were munching on too many leaves?"]
COUNTING_TWICE_RESPONCES = ["Hey there, (user) is a counting champion! Two correct numbers in a row, you should let others count too!"
, "(user) forgot that they wern't suppost to put two numbers in a row, so they did it."
, "(user) counted twice in a row! They weren't supposted to do that."
, "Whoa Nelly! You're counting like a champ, but remember, sharing is caring (and counting is more fun with friends)!"
, "Woah there, (user), counting superstar! Don't hog all the numbers, let others have a turn!"
, "Fweh! Did someone forget to count the yummy red panda berries in between? We can't miss any snacks, but only one at a time!"
, "Nom nom nom... wait, didn't we just count something delicious? Maybe (user) needs a paw-sicle break from counting two in a row!"]


with open('ReactionRolesNames.txt', 'r') as file:
  # Read all lines at once (check if any lines exist)
  lines = file.readlines()
  if not lines:
    1 == 1
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
    1 == 1
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
    
def set_current_number():
  with open('currentnumber.txt', 'r') as currentnumberfile:
    lines = currentnumberfile.readlines()
    for line in lines:
      number = line.strip()
      CURRENT_NUMBER.clear()
      CURRENT_NUMBER.append(int(number))

def set_last_author():
  with open('lastauthor.txt', 'r') as currentnumberfile:
    lines = currentnumberfile.readlines()
    if lines == []:
      author = "None"
      LAST_AUTHOR.clear()
      LAST_AUTHOR.append(author)
    for line in lines:
      author = line.strip()
      LAST_AUTHOR.clear()
      LAST_AUTHOR.append(author)
      
def create_funny_response_wrong_number(user_name, last_number):
  index = random.randint(0, len(WRONG_NUMBER_RESPONCES) - 1)
  index = random.randint(0, len(WRONG_NUMBER_RESPONCES) - 1)
  index = random.randint(0, len(WRONG_NUMBER_RESPONCES) - 1)
  index = random.randint(0, len(WRONG_NUMBER_RESPONCES) - 1)
  template = WRONG_NUMBER_RESPONCES[index]
  response = template.replace("(user)", user_name)
  if last_number is not None:
    response = response.replace("(last_number)", str(last_number))
  return response

def create_funny_response_count_twice(user_name, last_number):
  index = random.randint(0, len(COUNTING_TWICE_RESPONCES) - 1)
  index = random.randint(0, len(COUNTING_TWICE_RESPONCES) - 1)
  index = random.randint(0, len(COUNTING_TWICE_RESPONCES) - 1)
  index = random.randint(0, len(COUNTING_TWICE_RESPONCES) - 1)
  template = COUNTING_TWICE_RESPONCES[index]
  response = template.replace("(user)", user_name)
  if last_number is not None:
    response = response.replace("(last_number)", str(last_number))
  return response

set_current_number()
set_last_author()
  
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
async def on_member_join(member):
  channel = bot.get_channel(WELCOME_CHANNEL_ID)
  embed = discord.Embed(title="Welcome New User!!!!", description=f"Welcome to the discord server <@!{member.id}>!!")
  embed.add_field(name="Please read what is below!!", value="", inline=False)
  embed.add_field(name=f"Read the rules in: <#1246834677952806932>!", value="", inline=False)
  embed.add_field(name=f"Get your roles in: <#1246846297588240485>!", value="", inline=False)
  #embed.add_field(name=f"Verify your account in <#>!", value="", inline=False)
  embed.add_field(name=f"If you are interesting in working here view this channel! <#1246828297044627486>", value="", inline=False)
  await channel.send(member.mention, embed=embed)
    

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

@bot.tree.command(name="purge_messages", description="Delate messages(Only use when nessarry very dangerous!)")
@app_commands.describe(channel="What channel should I deleate messages in?")
@app_commands.describe(number="How many messages should I deleate?")
@app_commands.default_permissions(administrator=True)
@app_commands.guild_only()
async def purge_messages(interaction: discord.Interaction, channel: discord.TextChannel, number: int):
  await interaction.response.send_message(f"I will now deleate the messages in <#{channel.id}>", ephemeral=True)
  await channel.purge(limit=number)
  
@bot.tree.command(name="apply", description="Apply for a MR or HR postion at Bitebliss Cafe!")
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
        
        if HRQUESTIONS.index(question) + 1 == 9:
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
      await employemnt_message.add_reaction("✅")
      await employemnt_message.add_reaction("❌")

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
  embed=discord.Embed(title=f"{rank} Application results: Bitebliss Cafe", color=0x5fe06f)
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
  embed=discord.Embed(title=f"{rank} Application results: Bitebliss Cafe", color=0xff2222)
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
@app_commands.default_permissions(manage_messages=True)
@app_commands.guild_only()
async def say(interaction: discord.Interaction, thing_to_say: str, channel: discord.TextChannel):
  await interaction.response.send_message("The message is sent", ephemeral=True)
  await channel.send(thing_to_say)
  

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

  await main_channel.send("What is these reaction roles for?")
  def check(response_message):
    return response_message.author == interaction.user and response_message.channel == interaction.channel

  user_response = await bot.wait_for('message', check=check, timeout=60)
  if user_response:
    embed_title = user_response.content
    count = count + 2
  else:
    await main_channel.send("I didn't receive a response. Exiting the poll setup.")
    count = count + 1
    return
  
  await main_channel.send("Do you need to add what the roles are for?(Yes or No)")
  def check(response_message):
    return response_message.author == interaction.user and response_message.channel == interaction.channel

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
    def check(response_message):
      return response_message.author == interaction.user and response_message.channel == interaction.channel

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
    def check(response_message):
      return response_message.author == interaction.user and response_message.channel == interaction.channel

    user_response = await bot.wait_for('message', check=check, timeout=60)
    if user_response:
      role_names.append(user_response.content)
      REACTION_ROLES_ROLE_NAMES.append(user_response.content)
      count = count + 2
    else:
      await main_channel.send("I didn't receive a response. Exiting the poll setup.")
      count = count + 1
      return
    if addWhatIsRoleFor == "yes" : 
      await main_channel.send(f"What is this role for?")
      def check(response_message):
        return response_message.author == interaction.user and response_message.channel == interaction.channel

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
  if addWhatIsRoleFor == "yes": 
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

def is_countable(message):
  try:
    int(message)
    return True
  except ValueError:
    return False
  
def write_info(current_number, last_author):
  with open('currentnumber.txt', 'w') as currentnumberfile:
    currentnumberfile.write(str(current_number))
    currentnumberfile.close()
    
  
  with open('lastauthor.txt', 'w') as lastauthorfile:
    lastauthorfile.write(last_author)
    lastauthorfile.close()
  set_current_number()
  set_last_author()
  

@bot.event
async def on_message(message):
  if message.channel.id == 1246859232242827365:
    current_number = CURRENT_NUMBER[0]
    last_author = LAST_AUTHOR[0]
    if is_countable(message.content):
      if int(message.content) == current_number + 1:
        if last_author != "None":
          if message.author.display_name == last_author:
            
            await message.add_reaction("❌")
            responce = create_funny_response_count_twice(message.author.display_name, current_number)
            responce += "\n Counting will now start over at **one**!"
            await message.reply(responce)
            current_number = 0
            last_author = "None"
            write_info(current_number, last_author)
          else:
            if current_number == 99:
              current_number += 1
              last_author = message.author.display_name
              await message.add_reaction("💯")
              write_info(current_number, last_author)
            else:
              current_number += 1
              last_author = message.author.display_name
              await message.add_reaction("✅")
              write_info(current_number, last_author)
        else:
          if current_number == 99:
            current_number += 1
            last_author = message.author.display_name
            await message.add_reaction("💯")
            write_info(current_number, last_author)
          else:
            current_number += 1
            last_author = message.author.display_name
            await message.add_reaction("✅")
            write_info(current_number, last_author)
      else:
        last_author = "None"
        await message.add_reaction("❌")
        responce = create_funny_response_wrong_number(message.author.display_name, current_number)
        responce += "\n Counting will now start over at **one**!"
        await message.reply(responce)
        current_number = 0
        write_info(current_number, last_author)


bot.run(BOT_TOKEN)
