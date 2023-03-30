import re

text = "00-999"
pattern = re.compile(r"\d\d-\d\d\d")

print(pattern.findall(text))
