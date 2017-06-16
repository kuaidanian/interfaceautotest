import sys
import time
import unittest
#from db_fixture import test_data
from src.common.HTMLTestRunner import HTMLTestRunner
from config import globalparam
from src.common import Mailpost
from src.common.log import Log

sys.path.append('./src/interface')
sys.path.append('./db_fixture')
# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './src/interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

def run():
    logger = Log()
    print(u"开始运行脚本:")
    logger.info(u"开始运行脚本:")
    if globalparam.isNeedCreateTestResult == 1:
        # test_data.init_data()  # 初始化接口测试数据
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filename = './report/htmlreport/' + now + '_result.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp,
                                title='RKYSB2G Interface Test Report',
                                description=u'用例执行情况')
        runner.run(discover)
        fp.close()
    else:
        print("不生成测试报告")
        unittest.main()
    Mailpost.sendreport()
    logger.info(u"运行完成退出~~~~~~~~~~~")
    print(u"运行完成退出~~~~~~~~~~~")

def run_all_testcase():
    # 执行测试套件
    # 添加定时器
    k = 0
    while k < globalparam.runcount:
        timing = time.strftime('%H_%M', time.localtime(time.time()))
        if globalparam.isneedtimeset == 1:
            if timing == globalparam.runtime:
                run()
                k = k + 1
            else:
                time.sleep(globalparam.sleeptime)
                print(timing)
        else:
            run()
            k = k + 1

if __name__ == "__main__":
    run_all_testcase()
