#coding=utf-8
import time
import os
from src.common import readconfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = readconfig.ReadConfig(os.path.join(config_file_path, 'config.ini'))
# 项目参数设置
prj_path = read_config.getValue('projectConfig', 'project_path')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'htmlreport')
# 测试数据路径
data_path = os.path.join(prj_path, 'db_fixture', 'testdata')
#是否需要定时设置
isneedtimeset = 0
#是否需要生成测试报告 1为是 其它为否
isNeedCreateTestResult = 1
#程序休眠时间
sleeptime = 5
#运行时间
runtime = '13_35'
#运行次数
runcount = 1
#测试报告存放路径
now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
testresultfilename = report_path + '\\' + 'TestResult' + now + '.html'
#邮件发送地址
mail_from_address = '18381671067@163.com'
#邮件接收地址
mail_accept_address = ['zhanghy@honor-go.com',
                       'lixd@honor-go.com',
                       '352584989@qq.com']
#是否需要发送邮件 1为是 其它为否
isneedsendMail = 0