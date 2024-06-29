"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""


def read_api_key():
    with open('./testBot/.APIkey.txt', 'r') as api_key:
        return api_key.read().strip()


def AI_bot(user_message):
  HISTORY = []

  # Read history from file efficiently
  try:
    with open("history.txt", 'r') as history_file:
      current_role = 0
      lines = history_file.readlines()
      for line in lines:
        if current_role == 0:
          role = "user"
          current_role = 1
        else:
          role = "model"
          current_role = 0
        
        HISTORY.append({"role": role, "parts": [line.strip()]})
  except FileNotFoundError:
    pass  # Ignore if history file doesn't exist

  import google.generativeai as genai

  genai.configure(api_key=read_api_key())

  # Create the model (unchanged)
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }
  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
  ]

  model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="You are a human is responsible with talking with people. You should always be friendly and kind. I don't want you to sound like an AI. I want you to to sound exactly like a human. I also don't want you to give similar or identical responses to anything!",
  )

  # Prepare current user message for history
  current_user_message = {"role": "user", "parts": [user_message.strip()]}

  # If history exists, append it to the current message
  if HISTORY:
    HISTORY.append(current_user_message)
  else:
    HISTORY = [current_user_message]  # Start history with current message

  chat_session = model.start_chat(history=HISTORY)

  response = chat_session.send_message(user_message)

  # Update history with both user and model messages
  if not HISTORY:
    HISTORY.append(current_user_message)
  HISTORY.append({"role": "model", "parts": [response.text]})

  # Save updated history to file
  with open("history.txt", 'w') as history_file:
    for message in HISTORY:
      history_file.write(f"{message['role']}: {' '.join(message['parts'])}\n")

  return response.text
