import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print mo.group(1)    # 415
print mo.group(2)    # 555-4242
print mo.group(0)    # 415-555-4242
print mo.group()     # 415-555-4242
print mo.groups()    # ('415', '555-4242')
areaCode, mainNumber = mo.groups()
print areaCode       # 415
print mainNumber     # 555-4242


heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print mo1.group()    # Batman
mo2 = heroRegex.search(r'Tina Fey and Batman.')
print mo2.group()    # Tina Fey

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search(r'Batmobile lost a wheel.')
print mo.group()     # Batmobile
print mo.group(1)    # mobile

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print mo1.group()     # Batman
mo2 = batRegex.search('The Adventure of Batwoman')
print mo2.group()     # Batwoman

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventure of Batman')
print mo1.group()     # Batman
mo2 = batRegex.search('The Adventure of Batwoman')
print mo2.group()     # Batwoman
mo3 = batRegex.search('The Adventure of Batwowowowoman')
print mo3.group()     # Batwowowowoman

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print mo1.group()     # Batwoman
mo2 = batRegex.search('The Adventure of Batwowowowoman')
print mo2.group()
mo3 = batRegex.search('The Adventure of Batman')
print mo3 == None     # True


haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print mo1.group()     # HaHaHa
mo2 = haRegex.search('Ha')
print mo2 == None     # True

