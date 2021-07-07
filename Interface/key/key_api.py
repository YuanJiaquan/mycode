import requests

class ApiKey():

    def do_get(self,url, params=None, **kwargs):
        return requests.get(url, params=params, **kwargs)


    def do_post(self,url, json=None, **kwargs):
        return requests.post(url,json=json, **kwargs)

    def sw123(self,x):
        print(x)




if __name__ == '__main__':
    Ak=ApiKey()
    s={'city':'成都'}
    da=Ak.do_get('http://39.98.138.157:5000/api/getweather',params=s)
    print(da.text)