import requests
import os
def download_file(url):
    r = requests.get(url, allow_redirects=True)
    print('a')
    print(r.content)
    if(r.headers.get('content-type') !='application/pdf'):
        return 0
    if(r.content):
        open('file.pdf', 'wb').write(r.content)
        return 1
    return 0
def delete_file():
    os.remove("file.pdf")
    return 1
def write_file(content):
    f = open("status.txt", "w")
    f.write(content)
    f.close()