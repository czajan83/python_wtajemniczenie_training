import re

text = "czajosand@o2.pl"
pattern = re.compile(r".*\w\@.*\w\..*\w")

print(pattern.findall(text))
