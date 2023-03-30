import re

text = "czajosand@wp.pl.io"
pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")

print(pattern.findall(text))
