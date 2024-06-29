import requests

def read_api_key():
  with open('../Tokens/APIkeys/GeminiAPIkey.txt', 'r') as api_key:
    return api_key.read().strip()


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

# Example usage (replace 'YOUR_API_KEY' with your actual key if available publicly)
api_key = read_api_key()  # Replace with your Gemini API key (if available)
question = input("Ask google gemini a question: ")
answer = ask_gemini(question, api_key)
print(answer)
