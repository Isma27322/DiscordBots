import nltk
from nltk.corpus import wordnet as wn
from nltk.sentiment import SentimentIntensityAnalyzer
from random import choice, weighted_choice

# Download necessary resources from NLTK
nltk.download('vader_lexicon')  # Sentiment analysis lexicon
nltk.download('punkt')        # Sentence tokenizer

def generate_response(message):
  """
  This function analyzes a message and generates a response.

  Args:
      message: The message to be analyzed (string)

  Returns:
      A response string
  """

  # Preprocess the message (lowercase, remove punctuation)
  message = message.lower()
  message = ''.join([c for c in message if c.isalnum() or c.isspace()])

  # Extract keywords (split on whitespace)
  keywords = message.split()

  # Sentiment analysis
  sentiment_analyzer = SentimentIntensityAnalyzer()
  sentiment = sentiment_analyzer.polarity_scores(message)

  # Choose response based on sentiment (optional)
  # You can use sentiment to tailor the response further (e.g., empathetic for negative)

  # Train a bigram language model on the message (limited data, but a starting point)
  tokens = nltk.word_tokenize(message)
  bigram_model = nltk.ngrams(tokens, 2)
  freq_dist = nltk.FreqDist(bigram_model)

  # Generate a response continuation using the bigram model
  response_start = message.split()[-1]  # Use the last word as the starting point
  response = response_start
  num_words = 3  # Number of words to generate (adjust as needed)
  for _ in range(num_words):
    probabilities = [freq_dist.get((response_start, word)) for word in wn.synsets(response_start)]
    next_word = choice(list(wn.synsets(response_start))[0].lemmas()) if not probabilities else choice(weighted_choice(probabilities))  # Choose based on probability or randomly (if no probability data)
    response += " " + next_word
    response_start = next_word

  # Combine message and generated response
  full_response = message + " " + response

  return full_response

# Example usage
message = "I'm bored, what can I do?"
response = generate_response(message)
print(response)
