import requests
import random
import json

def translate_zh_to_en(question, token):
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + token

    from_lang = 'auto'
    to_lang = 'en'
    term_ids = ''

    # Build request
    headers = {'Content-Type': 'application/json'}
    payload = {'q': question, 'from': from_lang, 'to': to_lang, 'termIds' : term_ids}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    return result["result"]["trans_result"][0]["dst"]

if __name__ == "__main__":
    print(translate_zh_to_en("你好啊！"))