import re

def re_strip(s, t=r'\s'):
    sb_re = re.compile('^' + t + '+')
    st_re = re.compile(t + '+' + '$')
    s = sb_re.sub('', s)
    s = st_re.sub('', s)
    return s

print re_strip('    f    ')
print re_strip('aaaafaaaa', 'a')

