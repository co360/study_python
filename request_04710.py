import requests

def getData():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    data = {'first': 'false', 'pn': 2, 'kd': 'Python'}
    header = {
        'Host': 'www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.lagou.com/jobs/list_Python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Anit-Forge-Token': 'None',
        'X-Anit-Forge-Code': '0',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '26',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=ABAAABAAAGFABEF5F42DDC6B803C77E84C4AAC5A7EF49C9; X_HTTP_TOKEN=e79f57ac3a46ebbd8315884551e427808f35f167eb; _ga=GA1.2.1229867395.1554885071; _gat=1; user_trace_token=20190410163109-fe08e3bd-5b6a-11e9-8db8-5254005c3644; LGSID=20190410163109-fe08e4c0-5b6a-11e9-8db8-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20190410163218-26cdde1f-5b6b-11e9-ae00-525400f775ce; LGUID=20190410163109-fe08e666-5b6a-11e9-8db8-5254005c3644; _gid=GA1.2.1189081200.1554885071; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=search_code; SEARCH_ID=a575c2246e97473eaa7e70fe5afe33a7; X_MIDDLE_TOKEN=5de3d3b85cf1d8ae94286af8da2d00ab'
    }
    res = requests.post(url, data=data, headers=header)
    res.encoding = 'utf-8'
    print res.json()


if __name__ == "__main__":
    getData()
