def success(text):
  print(text + " ✔")

def failure(text, hard_exit=True):
  print(text + " ❌")

  if hard_exit:
    exit()