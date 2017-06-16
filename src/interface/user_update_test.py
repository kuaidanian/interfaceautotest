import unittest
import requests
import os, sys
import json
from urllib.parse import urlencode
from src.common.log import Log

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class user_login_Test(unittest.TestCase):
    '''用户信息更新接口'''

    def setUp(self):
        data = {'service': 'user_update',
                'partner': 'ca4e1e00b4a0400cbd20fd8d82076551',
                'sign': '543534534132132',
        }
        self.base_url = "http://192.168.1.19:9984/openapi/getway?" + urlencode(data)

    def tearDown(self):
        print(self.result)

    def test_user_update_all_null(self):
        '''所有参数为空'''
        Log().info("开始执行测试用例test_user_login_all_null")
        payload = '&request={"platUserId":""}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], '请求参数不完整:platUserId')

    def test_user_update_password_null(self):
        '''修改登录密码--空原始密码新密码'''
        Log().info("开始执行测试用例test_user_update_password_null")
        payload = '&request={"platUserId":"1609260937392541000000002","ologinPwd":"","loginPwd":""}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['updateMsg'], '修改成功')

    def test_user_update_oldpassword_null(self):
        '''修改登录密码--空原始密码'''
        Log().info("开始执行测试用例test_user_login_platUserAccount_null")
        payload = '&request={"platUserId":"1609260937392541000000002","ologinPwd":"","loginPwd":"123456"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], '修改登录密码需要同时输入原密码和新密码')

    def test_user_login_platUserAccount_error(self):
        '''修改登录密码--空修改后密码'''
        Log().info("开始执行测试用例test_user_login_platUserAccount_error")
        payload = '&request={"platUserId":"1609260937392541000000002",' \
                  '"ologinPwd":"123456","loginPwd":""}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], '修改登录密码需要同时输入原密码和新密码')

    def test_user_login_ologinPwd_error(self):
        '''修改登录密码--原始密码错误'''
        Log().info("开始执行测试用例test_user_login_ologinPwd_error")
        payload = '&request={"platUserId":"1609260937392541000000002",' \
                  '"ologinPwd":"1234567","loginPwd":"123456"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['updateMsg'], '原登录密码错误')

    def test_user_login_loginPwd_toosmall(self):
        '''修改登录密码--新密码过短'''
        Log().info("开始执行测试用例test_user_login_loginPwd_toosmall")
        payload = '&request={"platUserId":"1609260937392541000000002","ologinPwd":"123456","loginPwd":"1"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['updateMsg'], '登录密码长度应在6-20位之间')

    def test_user_login_loginPwd_toolong(self):
        '''修改登录密码--新密码过长'''
        Log().info("开始执行测试用例test_user_login_loginPwd_toolong")
        payload = '&request={"platUserId":"1609260937392541000000002",' \
                  '"ologinPwd":"123456","loginPwd":"132112321321321132132212313211323232213"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['updateMsg'], '登录密码长度应在6-20位之间')

    def test_user_login_password_success(self):
        '''修改登录密码--修改成功'''
        Log().info("开始执行测试用例test_user_login_password_success")
        payload = '&request={"platUserId":"1609260937392541000000002",' \
                  '"ologinPwd":"123456","loginPwd":"1234567"}'
        payloadreturn = '&request={"platUserId":"1609260937392541000000002",' \
                  '"ologinPwd":"1234567","loginPwd":"123456"}'
        urltest = 'http://192.168.1.19:9984/openapi/getway?&service=user_login&partner=ca4e1e00b4a0400cbd20fd8d82076551&request={"platUserAccount": "weizhaojg", "password": "1234567"}&sign=543534534132132'
        url = self.base_url + payload
        urlreturn = self.base_url +payloadreturn
        requests.get(url)
        rtest = requests.get(urltest)
        self.result = rtest.json()
        testresult = json.loads(self.result)
        platuserid = testresult['responseData']['platUserId']
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['loginMsg'], '成功')
        self.assertEqual(platuserid, '1609260937392541000000002')
        self.assertEqual(testresult['responseData']['loginStatus'], 'T')
        requests.get(urlreturn)


if __name__ == '__main__':
    unittest.main()
