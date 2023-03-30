import re

text = "CDa3ł"
pattern = re.compile(r"[A-Z]{2}-?\w{3}")

print(pattern.findall(text))
