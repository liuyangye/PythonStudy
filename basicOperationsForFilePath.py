import os

print os.path.join('usr', 'bin', 'spam')   # usr/bin/spam

# output:
# /Users/liuyangye/accounts.txt
# /Users/liuyangye/details.csv
# /Users/liuyangye/invite.docx
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filenames in myFiles:
    print os.path.join('/Users/liuyangye',filenames)


# get current path
print os.getcwd()   # /Users/liuyangye/Desktop
os.chdir('/Users/liuyangye/Workspace/PythonStudy')
print os.getcwd()   # /Users/liuyangye/Workspace/PythonStudy
os.chdir('/Users/liuyangye/Desktop')
print os.getcwd()   # /Users/liuyangye/Desktop


# make new directory
os.makedirs('/Users/liuyangye/Desktop/tmpForTest/delicious/oranges')


# show absolute and relative path
print os.path.abspath('.')   # /Users/liuyangye/Desktop
print os.path.isabs('.')     # False
print os.path.isabs(os.path.abspath('.'))  # True
print os.path.relpath('/Users/liuyangye/Desktop', '/Users/')   # liuyangye/Desktop

path = '/Users/liuyangye/Workspace/PythonStudy'
print os.path.basename(path)       # PythonStudy
print os.path.dirname(path)        # /Users/liuyangye/Workspace
calcFilePath = '/Users/liuyangye/Workspace/PythonStudy'
print os.path.split(calcFilePath)  # ('/Users/liuyangye/Workspace', 'PythonStudy')


# check files' sizes and contents
totalSize = 0
for filename in os.listdir('/Users/liuyangye/Workspace/PythonStudy'):
    totalSize = totalSize + os.path.getsize(os.path.join('/Users/liuyangye/Workspace/PythonStudy', filename))
print totalSize

