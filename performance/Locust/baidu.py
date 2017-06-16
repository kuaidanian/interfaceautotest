from locust import HttpLocust, TaskSet, task
import urllib

class UserBehavior(TaskSet):

    @task(1)
    def baidu(self):
        self.client.get("/")

    @task(2)
    def login(self):
        url_login = 'http://192.168.1.19:9984/openapi/getway?'
        # 自定义请求头
        login_data = {"platUserAccount": "weizhaojg", "password": "123456"}
        values = {'service': 'user_login',
                  'partner': 'ca4e1e00b4a0400cbd20fd8d82076551',
                  'request': login_data,
                  'sign': '543534534132132'}
        header_login = {'Accept': 'application/json, text/javascript, */*; q=0.01', 'Origin': 'http://www.cmall.com',
                        'X-Requested-With': 'XMLHttpRequest',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Referer': 'http://www.cmall.com/login.new.html', 'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
                        'Cookie': 'JSESSIONID=DD9B749D7BE1CA3BC15F7C0E83D47D31; JSESSIONID=FD38BBF22C8F4D663938218A16AA0FEB; cartcount_isview=true; cartCheckList=401969; _ga=GA1.2.198003739.1475039942; _gat=1; Hm_lvt_6b905f228492484ca5d757ea626ddfbd=1474373126,1474519323,1474861167,1474874008; Hm_lpvt_6b905f228492484ca5d757ea626ddfbd=1475039942'}
        # 访问登录页面
        data = urllib.parse.urlencode(values)
        url_login += data
        userlogin = self.client.get(url_login, headers=header_login)
        #print(userlogin.url)
        '''当只输出response时，返回的是状态码：<Response [200]>'''
        # 输出json格式的返回值
        print(userlogin.json())
        #self.client.get('http://192.168.1.19:9984/openapi/getway?service=user_login&partner=ca4e1e00b4a0400cbd20fd8d82076551&request={"platUserAccount":"weizhaojg","password":"123456"}&sign=543534534132132')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000