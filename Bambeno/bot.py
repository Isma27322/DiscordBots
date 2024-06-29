import discord
from discord import app_commands
from discord.ext import commands
import random

def read_bot_token():
  with open('../Tokens/BambenoToken.txt', 'r') as file:
    return file.read().strip()


BOT_TOKEN = read_bot_token()
CURRENT_NUMBER = [0]
LAST_AUTHOR = []
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
      
set_current_number()
set_last_author()

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

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Hello world")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)
    
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
  if message.channel.id == 1246554751659675718:
    current_number = CURRENT_NUMBER[0]
    last_author = LAST_AUTHOR[0]
    if is_countable(message.content):
      if int(message.content) == current_number + 1:
        if last_author != "None":
          if message.author.display_name == last_author:
            
            await message.add_reaction("<:xmark:1240830446355353664>")
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
              await message.add_reaction("<:checkmark:1240830355984875561>")
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
            await message.add_reaction("<:checkmark:1240830355984875561>")
            write_info(current_number, last_author)
      else:
        last_author = "None"
        await message.add_reaction("<:xmark:1240830446355353664>")
        responce = create_funny_response_wrong_number(message.author.display_name, current_number)
        responce += "\n Counting will now start over at **one**!"
        await message.reply(responce)
        current_number = 0
        write_info(current_number, last_author)

@bot.event
async def on_message_delete(message):
  if message.channel.id == 1246554751659675718:
    channel = await bot.fetch_channel(1246554751659675718)
    # Check if the message was deleted by the bot itself
    if is_countable(message.content):
      current_number = CURRENT_NUMBER[0]
      if message.author.display_name == LAST_AUTHOR[0]:
        await channel.send(f"⚠️ <@{message.author.id}> deleted their number!!! ```{current_number}``` The next number is **{current_number+1}**")
    
    

bot.run(BOT_TOKEN)