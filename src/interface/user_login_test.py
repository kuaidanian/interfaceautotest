import unittest
import requests
import os, sys
import json
from urllib.parse import urlencode
from src.common.log import Log


parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class user_login_Test(unittest.TestCase):
    '''用户登陆接口'''

    def setUp(self):
        data = {'service': 'user_login',
                'partner': 'ca4e1e00b4a0400cbd20fd8d82076551',
                'sign': '543534534132132',
        }
        self.base_url = "http://192.168.1.19:9984/openapi/getway?" + urlencode(data)

    def tearDown(self):
        print(self.result)

    def test_user_login_all_null(self):
        '''所有参数为空'''
        Log().info("开始执行测试用例test_user_login_all_null")
        payload = '&request={"platUserAccount": "", "password": ""}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], '请求参数不完整:platUserAccount')


    def test_user_login_apassword_null(self):
        '''密码为空'''
        Log().info("开始执行测试用例test_user_login_apassword_null")
        payload = '&request={"platUserAccount": "weizhaojg", "password": ""}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], '请求参数不完整:password')

    def test_user_login_platUserAccount_null(self):
        '''登陆账户为空'''
        Log().info("开始执行测试用例test_user_login_platUserAccount_null")
        payload = '&request={"platUserAccount": "", "password": "123456"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], '请求参数不完整:platUserAccount')

    def test_user_login_platUserAccount_error(self):
        '''登陆账户不存在'''
        Log().info("开始执行测试用例test_user_login_platUserAccount_error")
        payload = '&request={"platUserAccount": "weizhao", "password": "123456"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['loginMsg'], '账号不存在')

    def test_user_login_password_error(self):
        '''登陆密码错误'''
        Log().info("开始执行测试用例test_user_login_password_error")
        payload = '&request={"platUserAccount": "weizhaojg", "password": "1234561"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['loginMsg'], '密码错误')

    def test_user_login_password_success(self):
        '''登陆成功'''
        Log().info("开始执行测试用例test_user_login_password_error")
        payload = '&request={"platUserAccount": "weizhaojg", "password": "123456"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        platuserid = testresult['responseData']['platUserId']
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['loginMsg'], '成功')
        self.assertEqual(platuserid, '1609260937392541000000002')
        self.assertEqual(testresult['responseData']['loginStatus'], 'T')
        return platuserid


if __name__ == '__main__':
    unittest.main()
