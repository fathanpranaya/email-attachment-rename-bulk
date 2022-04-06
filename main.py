import time
import os
import re
import shutil

if __name__ == '__main__':
    # variable to check same sender email address
    existing_files = []

    # list all files in current directory
    files = os.listdir('input')

    # check if output folder exists or not
    if os.path.exists('output'):
        # empty output folder
        shutil.rmtree('output')

    # create output folder
    os.mkdir('output')

    for file in files:
        # extract email from filename
        email = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', file)

        # if email is found
        if email:
            # get format of file
            fmt = re.search(r'\.(\w+)$', file)

            new_filename = email.group(0) + '.' + fmt.group(1)
            # add counter on the new_filename if the file already exists
            if new_filename in existing_files:
                new_filename = email.group(0) + '_' + str(existing_files.count(new_filename)) + '.' + fmt.group(1)

            # debugging
            print(f'{file[-30:]} --> {new_filename}')

            # copy file to output folder
            shutil.copy(f'input/{file}', f'output/{new_filename}')
            existing_files.append(new_filename)

    print(f'Renaming success: {len(files)} files')
