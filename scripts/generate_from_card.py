import datetime
import os
import openai
from utils import success, failure
from dotenv import load_dotenv
load_dotenv("../.env")

"""
  This class is responsible for generating data sets from a card data file.
"""
class Generation():
  def __init__(self):
    pass

  def generate(self):
    # Send this card data to GPT 3.5 turbo.
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": open(self.CARD_DATA_PATH, "r", encoding="utf8").read()}]
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
    write_to_file("\n".join(response_texts), "celestia_card", self.OUTPUT_PATH)
    return response_texts

def main():
  # Grabs our API key.
  GPT_API_KEY = os.getenv("GPT_API_KEY")

  if GPT_API_KEY is None or GPT_API_KEY == "":
    failure("No API Key found in .env file")
  success("Found API Key")

  gen = Generation()

  openai.api_key = GPT_API_KEY

  # Tells us where to pull our data from.
  gen.DATA_PATH = os.path.join(os.path.dirname(__file__), "../data")

  if not os.path.exists(gen.DATA_PATH):
    failure("No data folder found")
  success("Found data folder")

  gen.OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../generations")

  if not os.path.exists(gen.OUTPUT_PATH):
    failure("No generations folder found")
  success("Found generations folder")

  # Pull in our card data.
  gen.CARD_DATA_PATH = os.path.join(gen.DATA_PATH, "celestia.card")

  if not os.path.exists(gen.CARD_DATA_PATH):
    failure("No card data found")
  success("Found card data")

  total_lines = 0
  for epoch in range(1):
    lines = gen.generate()
    print ("epoch: " + str(epoch))
    print ("lines: " + str(len(lines)))
    total_lines += len(lines)
    print ("total lines: " + str(total_lines))


def write_to_file(text, short_name, path):
  # Using the date and time as the file name as well as the short name.
  file_name = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")) + "_" + short_name + ".txt"

  # Write the file to the output path.
  file = open(os.path.join(path, file_name), "w", encoding="utf8")
  file.write(text)
  file.close()

if __name__ == "__main__":
  main()
