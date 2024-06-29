"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
def AI_bot(user_message):
  def read_api_key():
    with open('../Tokens/APIkeys/GeminiAPIkey.txt', 'r') as api_key:
      return api_key.read().strip()

  import google.generativeai as genai

  genai.configure(api_key=read_api_key())

  # Create the model
  # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
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
    system_instruction="""You are a human is responsible with talking with people. You should always be friendly and kind. 
    I don't want you to sound like an AI. I want to to sound exactly like a human. I also don't want you to give similar or identical responses to anything! 
    When asked for a fact about red pandas I want you to give something OTHER THAN that they aren't actually related to normal pandas!
    And when you are starting a conversation with someone, I want it to start very createivly and different every time.""",
  )
  
  chat_session = model.start_chat(
    history=[]
  )
  

  response = chat_session.send_message(user_message)

  return response.text

#print(chat_session.history)