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
    '''创建订单'''

    def setUp(self):
        data = {'service': 'order_create',
                'partner': 'ca4e1e00b4a0400cbd20fd8d82076551',
                'sign': '543534534132132',
        }
        self.base_url = "http://192.168.1.19:9984/openapi/getway?" + urlencode(data)

    def tearDown(self):
        print(self.result)

    def test_order_create_success(self):
        '''创建订单成功'''
        Log().info("开始执行测试用例test_order_create_success")
        payload = '&request={"platUserId":""}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'F')
        self.assertEqual(testresult['errmsg'], '请求参数不完整:platUserId')




if __name__ == '__main__':
    unittest.main()
