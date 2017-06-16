# coding:gbk
import time
import urllib.request
import requests
import threading
from time import sleep

# ���ܲ���ҳ��
PERF_TEST_URL = "http://192.168.1.19:9981/?website=Flight"

# ����:ѹ������
# THREAD_NUM = 10            # �����߳�����
# ONE_WORKER_NUM = 500       #  ÿ���̵߳�ѭ������
# LOOP_SLEEP = 0.01      # ÿ������ʱ����(��)

# ����:ģ������״̬
THREAD_NUM = 10  # �����߳�����
ONE_WORKER_NUM = 10 # ÿ���̵߳�ѭ������
LOOP_SLEEP = 0.5  # ÿ������ʱ����(��)

# ������
ERROR_NUM = 0

# ����Ĵ�������������������
def doWork(index):
    t = threading.currentThread()
    # print ("["+t.name+" "+str(index)+"] "+PERF_TEST_URL)
    try:
       # html = urllib.request.urlopen(PERF_TEST_URL).read()
        url_login = 'http://192.168.1.19:9984/openapi/getway?'
        # �Զ�������ͷ
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
        # ���ʵ�¼ҳ��
        data = urllib.parse.urlencode(values)
        url_login += data
        userlogin = requests.get(url_login, headers=header_login)
        print(userlogin.url)
        '''��ֻ���responseʱ�����ص���״̬�룺<Response [200]>'''
        #print(userlogin)
        # ���json��ʽ�ķ���ֵ
        print(userlogin.json())
    except urllib.request.URLError as e:
        print("[" + t.name + " " + str(index) + "] ")
        print(e)
        global ERROR_NUM
        ERROR_NUM += 1

def working():
    t = threading.currentThread()
    print("[" + t.name + "] Sub Thread Begin")
    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        doWork(i)
        sleep(LOOP_SLEEP)
    print("[" + t.name + "] Sub Thread End")


def main():
    # doWork(0)
    # return
    t1 = time.time()
    Threads = []
    # �����߳�
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working, name="T" + str(i))
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

    print("main thread end")
    t2 = time.time()
    print("========================================")
    print("URL:", PERF_TEST_URL)
    print("��������:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
    print("�ܺ�ʱ(��):", t2 - t1)
    print("ÿ�������ʱ(��):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
    print("ÿ�����������:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
    print("��������:", ERROR_NUM)

if __name__ == "__main__":
    main()
