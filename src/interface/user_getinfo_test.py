import unittest
import requests
import os, sys
import json
from urllib.parse import urlencode
from src.common.log import Log
from src.interface import user_login_test

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class user_getinfo_Test(unittest.TestCase):
    '''获取用户信息'''

    def setUp(self):
        data = {'service': 'user_getinfo',
                'partner': 'ca4e1e00b4a0400cbd20fd8d82076551',
                'sign': '543534534132132',
        }
        self.base_url = "http://192.168.1.19:9984/openapi/getway?" + urlencode(data)

    def tearDown(self):
        print(self.result)

    def test_user_getinfo_all_null(self):
        '''所有参数为空'''
        Log().info("开始执行测试用例test_user_getinfo_all_null")
        payload = '&request={"platUserId":""}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], '请求参数不完整:platUserId')


    def test_user_getinfo_platuserid_null(self):
        '''platUserId不存在'''
        Log().info("开始执行测试用例test_user_login_apassword_null")
        payload ='&request={"platUserId":"331"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], '查询不到用户信息')

    def test_user_getinfo_platuserid_othercharacter(self):
        '''platUserId含有其它字符'''
        Log().info("开始执行测试用例test_user_login_platuserid_othercharacter")
        payload = '&request={"platUserId":"32121sdasd121"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], 'Input string was not in a correct format.')

    def test_user_getinfo_platuserid_toolong(self):
        '''platUserId过长'''
        Log().info("开始执行测试用例test_user_login_platUserAccount_error")
        payload = '&request={"platUserId":"15253523622512655214526553254125412523652536521452"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], 'Value was either too large or too small for a Decimal.')

    def test_user_getinfo_platuserid_success(self):
        '''platUserId成功查询'''
        Log().info("开始执行测试用例test_user_login_password_error")
        payload = '&request={"platUserId":"1609260937392541000000002"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['platUserAccount'], 'weizhaojg')


if __name__ == '__main__':
    unittest.main()
