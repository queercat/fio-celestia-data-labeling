import os
import openai
from utils import success, failure
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "../.env"))

def main():
  GPT_API_KEY = os.getenv("GPT_API_KEY")

  if GPT_API_KEY is None:
    failure("No GPT API key found.")
  success("Found GPT API key.")

  training_data_path = os.path.join(os.path.dirname(__file__), "../training_data/training_data.jsonl")

  if not os.path.exists(training_data_path):
    failure("No training data found.")
  success("Found training data.")

  resp = input("Are you sure you want to train? This will cost $$$ [y/(n)]: ")

  if resp.lower() != "y":
    failure("Aborting.")

if __name__ == "__main__":
  main()