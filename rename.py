import os
import re
import shutil

# list all files in current directory
files = os.listdir('input')
for file in files:
    # get format of file
    fmt = re.search(r'\.(\w+)$', file)
    # extract email from filename
    email = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', file)
    # if email is found
    if email:
        # debugging
        print(f'{file[-30:]} --> {email.group(0)}.{fmt.group(1)}')
        # copy file to output folder
        shutil.copy(f'input/{file}', f'output/{email.group(0)}.{fmt.group(1)}')

print(f'Renaming success: {len(files)} files')
