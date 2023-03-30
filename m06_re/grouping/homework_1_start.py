import re

text = "00-999"
pattern = re.compile(r"(\d{2})-(\d{3})")

print(pattern.findall(text))
