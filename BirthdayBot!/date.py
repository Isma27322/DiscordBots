import requests
from ai import AI_bot

def ask_question(question):
  """
  Simulates asking a question using Google search

  Args:
      question: The user's question

  Returns:
      A string containing the top search result for the question
  """
  def read_api_key():
    with open('../Tokens/APIkeys/GoogleAPIkey.txt', 'r') as google_api_key:
      return google_api_key.read().strip()
  # Encode the question for safe use in the URL
  encoded_question = requests.utils.quote(question)

  # Prepare the Google custom search API URL (replace with your own API key)
  url = f"https://www.googleapis.com/customsearch/v1?key={read_api_key()}&cx=94ee607515bb74272&q={encoded_question}"

  # Make the request and get the response
  response = requests.get(url)
  response.raise_for_status()  # Raise an error if request fails

  # Parse the JSON response
  data = response.json()

  # Extract the top search result (modify if you want more results)
  try:
    answer = data["items"][0]["snippet"]
  except (KeyError, IndexError):
    answer = "Sorry, I couldn't find an answer to your question."

  return answer

answer = ask_question("What is today's date?")

todays_date = AI_bot(f"Could you extract the date from this and only display the date? {answer}")

def get_date(days):
  Future_date = AI_bot(f"What date is {str(days)} days from {todays_date}. Only display the date But make to include the month date and year, MAKE SURE THERE IS NOTHING ELSE!!!!!!!")
  return Future_date