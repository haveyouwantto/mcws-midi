import requests

midi_mimetypes = ('audio/mid', 'audio/midi')

def download(url, mime):
    try:
        if not (url.startswith('http://') or url.startswith('https://')):
            url = 'http://' + url
        response = requests.get(url)
        
        if response.headers['Content-Type'] not in mime:
            return (1, response.headers['Content-Type'])

        filename = "midi/cache"
        
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)  # 将内容写入文件
            return (0,)
    except Exception as e:
        print(e)
        return (-1,)

def download_midi(url):
    return download(url, midi_mimetypes)