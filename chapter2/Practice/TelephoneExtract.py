import re

f = open("../data/telephone.txt", mode="rb")
result = f.read().decode().lower()
list = result.split()
print(list)
result = set()

def getPhoneNum(phone):
    regex = re.compile(r'1\d{10}', re.IGNORECASE)
    phonenums = re.findall(regex, phone)
    return len(phonenums) > 0

for phone in list:
    if getPhoneNum(phone):
        result.add(phone)
    else:
        continue

