
import undetected_chromedriver.v2 as uc
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random


# Thuê proxy az
api_proxyaz = 'e430e8eed7689fb7749af71c60884e68'

def get_proxy():
    # Tạo mới proxy
    print('Khởi tạo proxy mới')
    requests.get('https://proxy.shoplike.vn/Api/getNewProxy?access_token='+api_proxyaz)
    # Nhận proxy hiện tại
    ip = requests.get('https://proxy.shoplike.vn/Api/getCurrentProxy?access_token='+api_proxyaz).json()
    print('Proxy mới : '+ip['data']['proxy'])
    return ip['data']['proxy']




api_chothuesimcode = 'c9a2b43b'
### Thuê sim chothuesimcode
def get_sim():
    getsim = requests.get('https://chothuesimcode.com/api?act=number&apik='+api_chothuesimcode+'&appId=1090').json()
    if getsim['ResponseCode'] == 0:
        print('Thuê thành công số điện thoại : +84'+str(getsim['Result']['Number']))
        return [getsim['Result']['Id'],getsim['Result']['Number']]
    
    else :
        print('No sim !!!!!!!!!')


### Nhận code từ sim
def get_code(id):
    time.sleep(1)
    getcode = requests.get('https://chothuesimcode.com/api?act=code&apik='+api_chothuesimcode+'&id='+str(id)).json()
    if getcode['ResponseCode'] == 1:
        return get_code(id)
    elif getcode['ResponseCode'] == 0:
        print('Mã code veri số điện thoại : '+str(getcode['Result']['Code']))
        return getcode['Result']['Code']



options = uc.ChromeOptions()
options.add_argument(f'--proxy-server='+get_proxy())

driver = uc.Chrome(use_subprocess=True,options=options)
url = 'https://www.paypal.com/vn/welcome/signup/?locale.x=vi_VN'
driver.get(url)
time.sleep(100000)
   

