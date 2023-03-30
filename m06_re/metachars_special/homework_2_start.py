import re

text = "CD-a3ł"
pattern = re.compile(r"[A-Z][A-Z]-\w\w\w")

print(pattern.findall(text))
