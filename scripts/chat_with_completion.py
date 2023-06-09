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

  openai.api_key = GPT_API_KEY

  response = openai.Completion.create(
    model="curie:ft-personal-2023-06-09-09-05-53",
    temperature=0.8,
    max_tokens=150,
    top_p=1,
    stop=["\n","\r"],
    frequency_penalty=0.1,
    prompt="I'm really not enjoying my job, what should I do? ->"
  )

  print(response)



if __name__ == "__main__":
  main()