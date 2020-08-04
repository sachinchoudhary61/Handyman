import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"Zskx6DqtXCPViGOjYMznUl3K9eAQJahfTRpb152vu7rdEoFwgLSz0JFY7hWAKy19m4d8RqIoNswfHgXe","sender_id":"FSTSMS","language":"english","route":"p","numbers":"7018738324","message":"kasvo here biatchhh!!!!","variables":"{AA}|{CC}","variables_values":"12345|asdaswdx"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)