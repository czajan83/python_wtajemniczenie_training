import re

text = "00-999"
pattern = re.compile(r"[0-9][0-9]-[0-9][0-9][0-9]")

print(pattern.findall(text))
