import requests

def generateUrls():
    zodiac_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo',
                    'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
    urls = []

    for sun in zodiac_signs:
        for moon in zodiac_signs:
            url = sun + "-" + moon + ".pdf"
            urls.append(url)

    return urls


def url_response(url, name):
    path = name
    url = url + name
    r = requests.get(url, stream=True)

    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)


URL = "http://universal-tao-eproducts.com/mp/files/sun-moon_"
for i, url in enumerate(generateUrls()):
    url_response(URL, url)
