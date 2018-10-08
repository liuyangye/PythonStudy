import re

text = ['(021)88776543', '010-55667890', '02584453362', '057166345673']
for count in text:
    m = re.findall(r"\(?0\d{2,3}[)-]?\d{7,8}", count)
    if m:
      print m
    else:
      print 'not match'