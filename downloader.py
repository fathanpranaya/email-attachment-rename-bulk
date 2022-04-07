import os
import shutil
import requests

url_list = [
    {
        'email': 'drhestikartika@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/17A98FFF-6075-41CE-9B60-30BB9AF7EBA5_1649135764484958.jpeg'
    }, {
        'email': 'zahramlinda95@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/IMG_20220405_120036_889_1649136157653199.jpg'
    }, {
        'email': 'nuzululfirdaus5@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/024335B7-E0CC-4992-B02F-FD0B1C036C39_1649137148906706.jpeg'
    }, {
        'email': 'anjndts02@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/2021-10-24%2004.58.14%201_1649158690684903.jpg'
    }, {
        'email': 'Ulinnafis02@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/20220405000203617_save_1649167753047089.jpg'
    }, {
        'email': 'syifaamalia702@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/4A815C6A-D6B6-4AE5-908E-5833E71B9CD9_1649172217697794.jpeg'
    }, {
        'email': 'Marsalinajatiparastami@yahoo.co.id',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/08EBEA4D-9DE7-40B7-B422-BFCD3A50C698_1649173202970996.jpeg'
    }, {
        'email': 'Dewiegunawan35@yahoo.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/45F880AD-D3A9-4E5C-B7CA-1E702DD349F6_1649178039029060.jpeg'
    }, {
        'email': 'dessiianna159@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/13D4C900-7123-413F-A009-39E5F579F4EA_1649214957176758.png'
    }, {
        'email': 'ranirabbani@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/IMG_4077_1649224707642159.jpg'
    }, {
        'email': 'syafirasaniazulfa@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/6470F1A9-97C1-421E-ACD5-A3D289DE7352_1649229024582573.jpeg'
    }, {
        'email': 'marwahaspa.b12@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/FB555AB6-A5E4-4370-B1D4-E17FA81275DB_1649235867312555.jpeg'
    }, {
        'email': 'dindanrjh@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/5E097F7F-CA45-4425-93AE-996510C650F6_1649241233811992.jpeg'
    }, {
        'email': 'jrestikomah@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/4421D69A-75A0-4C70-8DA6-5D2215B58761_1649245032133877.jpeg'
    }, {
        'email': 'untarifitri@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/3877E5CD-0884-441E-A8EA-786A7670FB03_1649249028470173.jpeg'
    }, {
        'email': 'salsabilafatra@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/IMG_20220406_175443_1649249663962192.jpg'
    }, {
        'email': 'rizkyfebriwanti@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/C8C13182-5E0B-4122-BE93-ACFF5756ACE4_1649080118781665.jpeg'
    }, {
        'email': 'Rahmaizar.nina@gmail.com',
        'link': ' https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/41A25358-789E-483B-BDC7-8842BA07D975_1649085997406432.jpeg'
    }, {
        'email': 'grahmannisa@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/99194E75-92B3-4A69-A189-01A3BFC86D92_1649092578140447.jpeg'
    }, {
        'email': 'vindyv86@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/1970-01-20-100505787_1649124905897634.jpg'
    }, {
        'email': 'wildanur50@gmail.com',
        'link': 'https://tokotalk.s3.ap-southeast-1.amazonaws.com/images/orders/60BEF769-8B91-4C82-9418-E69A54F5FBB4_1649129306237116.jpeg'
    }
]

if __name__ == '__main__':
    # check if downloads folder exist
    if os.path.exists('downloads'):
        # empty downloads folder
        shutil.rmtree('downloads')
    # create downloads folder
    os.mkdir('downloads')

    # iterate url_list
    for url in url_list:
        # get server filename and new file_name using email
        filename = url.get("link").split("/")[-1]
        new_filename = f'{url.get("email")}.{filename.split(".")[-1]}'
        # Print for debugging
        print(f'Download {url.get("link")} -> downloads/{new_filename}')
        # HTTP Request
        r = requests.get(url.get("link"))
        # Store the response
        open(filename, 'wb').write(r.content)
        # Move the downloaded files to downloads folder
        os.rename(f'{filename}', f'downloads/{new_filename}')
