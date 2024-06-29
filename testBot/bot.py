import discord
from discord import app_commands
from discord.ext import commands
import requests

from Ai import AI_bot

def read_bot_token():
  with open('token.txt', 'r') as file:
    return file.read().strip()

def read_api_key():
  with open('.APIkey.txt', 'r') as api_key:
    return api_key.read().strip()

API_KEY = read_api_key()

BOT_TOKEN = read_bot_token()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

def ask_gemini(question, api_key):
  """
  This function sends a question to the hypothetical Gemini API using a POST request 
  with a JSON body similar to the provided curl command.
  """
  # Replace 'YOUR_API_KEY' with your actual Gemini API key (if available publicly)
  # and update the endpoint URL based on official documentation (when available).
  url = 'https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash' + ':generateContent?key=' + api_key
  headers = {'Content-Type': 'application/json'}
  data = {
    "contents": [
      {
        "role": "user",
        "parts": [
          {"text": question}
        ]
      }
    ]
  }
  response = requests.post(url, headers=headers, json=data)

  if response.status_code == 200:
    data = response.json()
    # Extract the answer from the response (assuming similar structure as example)
    if data['candidates']:
      answer = data['candidates'][0]['content']['parts'][0]['text']
      return answer
    else:
      return "I can't answer that yet, but I'm still learning."
  else:
    return f"API Error: {response.status_code}"

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
  conversation_exited = False
  # Check if the message is from the bot or not a ping
  if message.author == bot.user or not message.mentions.__contains__(bot.user):
    return
  print(message.content.strip("<@1224182938569150564>"))
  await message.channel.send("""To exit this conversation say "exit" at any time.""")
  message_striped_ping = message.content.strip("<@1224182938569150564>")
  question = f"Give a human like responce to this: {message_striped_ping}"
  answer = ask_gemini(question, API_KEY)
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
    question = f"Give a human responce to this: {user_response.content}"
    answer = ask_gemini(question, API_KEY)
    await user_response.reply(answer)
    answer = ""


bot.run(BOT_TOKEN)