import datetime
import os
import openai
from dotenv import load_dotenv
load_dotenv("../.env")

def success(text):
  print(text + " ✔")

def failure(text, hard_exit=True):
  print(text + " ❌")

  if hard_exit:
    exit()

def main():
  # Grabs our API key.
  GPT_API_KEY = os.getenv("GPT_API_KEY")

  if GPT_API_KEY is None or GPT_API_KEY == "":
    failure("No API Key found in .env file")
  success("Found API Key")

  openai.api_key = GPT_API_KEY

  # Tells us where to pull our data from.
  DATA_PATH = os.path.join(os.path.dirname(__file__), "../data")

  if not os.path.exists(DATA_PATH):
    failure("No data folder found")
  success("Found data folder")

  OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../generations")

  if not os.path.exists(OUTPUT_PATH):
    failure("No generations folder found")
  success("Found generations folder")

  # Pull in our card data.
  CARD_DATA_PATH = os.path.join(DATA_PATH, "celestia.card")

  if not os.path.exists(CARD_DATA_PATH):
    failure("No card data found")
  success("Found card data")

  # Send this card data to GPT 3.5 turbo.
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": open(CARD_DATA_PATH, "r", encoding="utf8").read()}]
  )

  if response is None:
    failure("No response from GPT3")

  choices = response["choices"]

  if choices is None or len(choices) == 0:
    failure("No choices in response")

  response_texts = []

  for choice in choices:
    # Extract the message from the choice.
    message = choice["message"]

    response_texts = message["content"].split("\n")

  # Write the response to a file.
  write_to_file("\n".join(response_texts), "celestia_card", OUTPUT_PATH)

def write_to_file(text, short_name, path):
  # Using the date and time as the file name as well as the short name.
  file_name = str(datetime.date.today()) + "_" + short_name + ".txt"

  # Write the file to the output path.
  file = open(os.path.join(path, file_name), "w", encoding="utf8")
  file.write(text)
  file.close()



if __name__ == "__main__":
  main()
