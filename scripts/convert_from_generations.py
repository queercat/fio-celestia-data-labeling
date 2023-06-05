"""
This script converts the generations into one large file to be used for training.
"""

import os
import sys

from utils import success, failure

def main():
  GENERATIONS_PATH = os.path.join(os.path.dirname(__file__), "../generations")

  if not os.path.exists(GENERATIONS_PATH):
    failure("No generations folder found")

  # Put all the files in a list.
  generations_list = os.listdir(GENERATIONS_PATH)

  for path in generations_list:
    path = os.path.join(GENERATIONS_PATH, path)

    if not os.path.isfile(path):
      failure("Not a file: " + path, False)
      continue

    objects = []

    with open(path, "r") as f:
      objects = convert_file_to_array(f)

    if len(objects) == 0:
      failure("Unable to generate objects")

    OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../training_data/")

    if not os.path.exists(OUTPUT_PATH):
      failure("No output directory.")

    # Write the objects to a file.
    with open(os.path.join(OUTPUT_PATH, "training_data.txt"), "a") as f:
      # Write each object as json to the file.
      for object in objects:
        f.write(str(object) + "\n")



def convert_file_to_array(file):
  """
  So we want to convert a file with a bunch of
  User: Lorem Ipsum/n
  CelestAI: Lorem Ipsum/n
  in an array of objects like this:
  [
    {
      "User": "Lorem Ipsum",
      "CelestAI": "Lorem Ipsum"
    }
  ]
  """
  objects = []
  object = {}

  # Read each line of the file.
  dirty_lines = file.readlines()
  lines = []

  for line in dirty_lines:
    line = line.lstrip()

    if line == "":
      continue

    lines.append(line)

  expects = ["User", "CelestAI"]
  value = 0
  def increment_value(v):
    if v == 0:
      return 1
    else:
      return 0

  for line in lines:
    if ":" not in line:
      continue
    if "User:" in line and value == 0:
      object["User"] = line.split("User:")[1].strip()
      value = increment_value(value)
    elif "CelestAI:" in line and value == 1:
      object["CelestAI"] = line.split("CelestAI:")[1].strip()
      value = increment_value(value)
      objects.append(object)
      object = {}
    else:
      continue

  return objects

if __name__ == "__main__":
  main()