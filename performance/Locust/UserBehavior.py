from locust import HttpLocust,TaskSet,task
import json


class UserBehavior(TaskSet):

    token = ''
    userId = ''
    headers = ''

    def login(self):
        data = {
            "Account": "weizhaojg",
            "passwd": "123456",
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'}
        url_login = 'http://192.168.1.19:9984/openapi/getway?service=user_login&partner=ca4e1e00b4a0400cbd20fd8d82076551&request={"platUserAccount":"weizhaojg","password":"123456"}&sign=543534534132132'
        response = self.client.post(
            url_login,
            headers=headers)
        content = json.loads(response.content)
        self.token = {"token": content['data']['token']}
        self.userId = content['data']['userId']

    def logout(self):
        url_login = 'http://192.168.1.19:9984/openapi/getway?service=user_login&partner=ca4e1e00b4a0400cbd20fd8d82076551&request={"platUserAccount":"weizhaojg","password":"123456"}&sign=543534534132132'
        with self.client.get(url_login, params=self.token, catch_response=True) as response:
            if response.status_code != 200:
                response.failure()

    def user_details(self):
        data = {'userId': self.userId}
        url_login = 'http://192.168.1.19:9984/openapi/getway?service=user_login&partner=ca4e1e00b4a0400cbd20fd8d82076551&request={"platUserAccount":"weizhaojg","password":"123456"}&sign=543534534132132'
        with self.client.get(url_login, params=data, headers=self.headers, catch_response=True) as response:
            if response.status_code != 200:
                response.failure()

    @task(10)
    def login_logout(self):
        self.login()
        self.user_details()
        self.logout()


class WebsiteUser(HttpLocust):
    host = 'http://192.168.1.19:9984/'
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000