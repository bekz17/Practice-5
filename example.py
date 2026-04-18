import re

text = "My phone number is 123-456-7890"

# search()
print(re.search(r"\d{3}-\d{3}-\d{4}", text))

# findall()
print(re.findall(r"\d+", text))

# split()
print(re.split(r"\s", text))

# sub()
print(re.sub(r"\d", "*", text))