import unittest
import requests
import os, sys
import json
from urllib.parse import urlencode
from src.common.log import Log

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

class flight_query_Test(unittest.TestCase):
    '''航班查询接口（待完善）'''

    def setUp(self):
        data = {'service': 'flight_query',
                'partner': 'ca4e1e00b4a0400cbd20fd8d82076551',
                'sign': '543534534132132',
        }
        self.base_url = "http://192.168.1.19:9984/openapi/getway?" + urlencode(data)

    def tearDown(self):
        print(self.result)

    def test_flight_getinfo(self):
        '''航班查询接口'''
        Log().info("开始执行测试用例test_flight_getinfo")
        payload = '&request={"airline":"CA","departureTime":"2017-05-22 00:00:00",' \
                  '"departurecity":"PEK",' \
                  '"arrivecity":"CTU",' \
                  '"bookreason":"1",' \
                  '"PlatCompanyId":"1609260937392691000000003"}'
        url = self.base_url + payload
        r = requests.get(url)
        self.result = r.json()
        testresult = json.loads(self.result)
        self.assertEqual(testresult['issuccess'], 'T')
        self.assertEqual(testresult['responseData']['updateMsg'], '登录密码长度应在6-20位之间')


if __name__ == '__main__':
    unittest.main()
