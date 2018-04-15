"""
Encoding a list of string and then decoding it
https://stackoverflow.com/questions/853475/whats-the-simplest-way-to-encoding-liststring-into-plain-string-and-decode-it
"""

def encoding(str_list):
  res = []
  for str in str_list:
    res.append(str.replace("|", "|,"))
  return "||".join(res)

def decoding(str):
  str_list = str.split("||")
  return [str.replace("|,", "|") for str in str_list]

print("str|".replace("|", "|,"))
print("||".join(["a"]))
