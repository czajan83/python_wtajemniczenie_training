import re

text = "https://www.softest.com"
pattern = re.compile(r"https?\:/{2}w{3}\..*\w\..*\w")

print(pattern.findall(text))
