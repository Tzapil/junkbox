import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import shutil
import re

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def validate(url):
    # // validate -> processVideo
    data = {
        'advSettings': False,
        'aspectRatio': "-1",
        'audioBitrate': 0,
        'audioFormat': None,
        'audioFrequency': 0,
        'channel': "stereo",
        'custom_resx': -1,
        'custom_resy': -1,
        'dummy': "1",
        'endTo': "-1",
        'fromConvert': "urlconverter",
        'id_process': None,
        'keyHash': None,
        'nbRetry': 0,
        'oldServerIds': [],
        'requestExt': "mp3",
        'serverId': None,
        'serverUrl': None,
        'startFrom': "-1",
        'title': None,
        'uploadPath': None,
        'urlEntryUser': url,
        'videoBitrate': None,
        'videoResolution': "-1",
        'volume': 0
    }
    r = requests.post('https://www2.onlinevideoconverter.com/webservice', verify=False, data={
        'function': 'validate',
        **{'args[' + n + ']': data[n] for n in data}
    })

    return r.json()['result']

def process(url, raw_data):
    # // validate -> processVideo
    data = {
        'dummy': "1",
        'urlEntryUser': url,
        'fromConvert': "urlconverter",
        'requestExt': "mp3",
        'serverId': raw_data['serverId'],
        'nbRetry': 0,
        'title': raw_data['title'],
        'keyHash': raw_data['keyHash'],
        'serverUrl': raw_data['serverUrl'],
        'id_process': raw_data['id_process'],
        'videoResolution': "-1",
        'audioBitrate': 0,
        'audioFrequency': 0,
        'channel': "stereo",
        'volume': 0,
        'startFrom': "-1",
        'endTo': "-1",
        'custom_resx': -1,
        'custom_resy': -1,
        'advSettings': False,
        'aspectRatio': "-1"
        
        
    }
    r = requests.post('https://www2.onlinevideoconverter.com/webservice', verify=False, data={
        'function': 'processVideo',
        **{'args[' + n + ']': data[n] for n in data}
    })

    return r.json()['result']

def get_success_page(page_id):
    r = requests.post('https://www.onlinevideoconverter.com/success', verify=False, data={'id': page_id})
    res = re.search(r'class=\"download\-button\" href=\"(https:\/\/.*?)\"', r.text)
    return res[1]

def get_link(url):
    link = ''
    raw_data = validate(url)
    status = raw_data['status']
    if status == 'failed':
        print('FAILED', raw_data)
    elif status == 'default':
        # print('DEFAULT', raw_data)
        # link = raw_data['serverUrl'] + '/download?file=' + raw_data['dPageId']
        link = get_success_page(raw_data['dPageId'])
    else:
        # print(result)
        result = process(url, raw_data)
        link = get_success_page(result['dPageId'])
        # link = raw_data['serverUrl'] + '/download?file=' + result['id_process']

    return link

# def download(url):
#     r = requests.get(url, verify=False, stream=True)
#     if r.status_code == 200:
#         with open('file.mp3', 'wb') as f:
#             r.raw.decode_content = True
#             shutil.copyfileobj(r.raw, f)

link = get_link('https://youtu.be/x2pXP0U__6Y')
print(link)
# download(link)

