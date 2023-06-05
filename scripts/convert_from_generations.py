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

if __name__ == "__main__":
  main()