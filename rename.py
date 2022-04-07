import time
import os
import re
import shutil

if __name__ == '__main__':
    # variable to check same sender email address
    existing_email = []

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

            # add counter on the new_filename if the file already exists
            new_email = email.group(0)
            if new_email in existing_email:
                new_filename = new_email + '_' + str(existing_email.count(new_email)) + '.' + fmt.group(1)
            else:
                new_filename = new_email + '.' + fmt.group(1)

            # debugging
            # print(f'{cnt} {file[-30:]} --> {new_filename}')

            # copy file to output folder
            res = shutil.copy(f'input/{file}', f'output/{new_filename}')


            print(f'copying file: {res}')
            existing_email.append(new_email)
        else:
            print(f'cannot rename {file}')

    print(f'Renaming success: {len(files)} files')








