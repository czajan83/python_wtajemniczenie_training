import re

text = "CD-a3Z"
pattern = re.compile(r"[A-Z][A-Z]-[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]")

print(pattern.findall(text))
