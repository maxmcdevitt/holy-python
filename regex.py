import re

with open("woods.py", 'r') as w:
    wds = w.read()

pattern = re.compile(r'("\S")')
matches = pattern.finditer(wds)
for m in matches:
    print(m)
pattern2 = re.compile(r'^(' ')')
matches2 = pattern2.finditer(wds)
#pattern = re.compile(r'^(".\S")$')

for m in matches2:
    print(m)

