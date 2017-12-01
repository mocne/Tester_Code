# -*- coding: utf-8 -*-

import requests

def requestWithMethodAndParams(method, url, params, isJson):
    session = requests.session()
    if method == 'GET':
        finaUrl = url + '?currentPage=' + params['data']['currentPage'] + '&pageSize=' + params['data']['pageSize'] + '&flag=' + params['data']['flag']
        result = session.get(url=finaUrl).json()
        if isJson:
            return result
        return result
    elif method == 'POST':
        result = session.post(url=url, data=params['data'], cookies=params['cookies'])
        if isJson:
            return result.json()
        return result
    else:
        return 'Unknown request method !'

if __name__ == '__main__':
    Url = 'http://a.cnaidai.com/webjr/invest/investListService.cgi'
    Method = 'GET'
    Params = {
        'data': {
            'currentPage': '1',
            'pageSize': '5',
            'flag': '8',
            'timeLimitType': '',
            'aprType': '',
            '_': ''
        },
        'cookies': [],
    }
    IsJson = True
    a = requestWithMethodAndParams(method=Method, url=Url, params=Params, isJson=IsJson)
    print(a)