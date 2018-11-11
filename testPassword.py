import re, pyperclip

len_re = re.compile(r'.{8,}')
char_re = re.compile(r'[a-z].*[A-Z]|[A-Z].*[a-z]')
num_re = re.compile(r'\d')

def passwordTest(password):
    if len_re.search(password) and char_re.search(password) and num_re.search(password):
        print 'Your passwordd is strong enough!'
    else:
        print 'Your password is weak, please reset'

password = str(pyperclip.paste())
passwordTest(password)

