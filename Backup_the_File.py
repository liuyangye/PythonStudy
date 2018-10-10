import os
import time

source = r'C:\Workspace\TempforTest'
print source
target_dir = 'C:\\Backup\\'
print target_dir

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr \"%s\" %s" % (target, ''.join(source))
print zip_command

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'