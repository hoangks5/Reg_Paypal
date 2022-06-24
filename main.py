
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


while True:
    options = uc.ChromeOptions()
    options.add_argument(f'--proxy-server='+get_proxy())

    driver = uc.Chrome(use_subprocess=True,options=options)
    url = 'https://www.paypal.com/vn/welcome/signup/?locale.x=vi_VN'
    driver.get(url)
    time.sleep(random.randint(1,3))
    sim = get_sim()
    driver.find_element_by_id('paypalAccountData_phone').send_keys(sim[1])
    time.sleep(random.randint(1,3))
    driver.find_element_by_id('paypalAccountData_submit').click()
    code_veri_sdt = get_code(sim[0])
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div/div/form/fieldset/div[3]/div[1]/div/div[1]/input').send_keys(code_veri_sdt)
    time.sleep(random.randint(1,3))
    mail = open('mail.txt','r',encoding='utf-8').read().splitlines()[0].split('|')[0]
    driver.find_element_by_id('paypalAccountData_email').send_keys(mail)
    driver.find_element_by_id('paypalAccountData_lastName').send_keys(random.choice(open('data/ho','r',encoding='utf-8').read().splitlines()))
    driver.find_element_by_id('paypalAccountData_middleName').send_keys(random.choice(open('data/ten','r',encoding='utf-8').read().splitlines()))
    driver.find_element_by_id('paypalAccountData_firstName').send_keys(random.choice(open('data/ten','r',encoding='utf-8').read().splitlines()))
    pw = '@Hoang'+str(random.randint(1000,9999))
    driver.find_element_by_id('paypalAccountData_password').send_keys(pw)
    driver.find_element_by_id('paypalAccountData_confirmPassword').send_keys(pw)
    print('Tài khoản: '+mail)
    print('Mật khẩu : '+pw)


    read_acc = open('fullacc.txt','r',encoding='utf-8').read().splitlines()
    read_acc.append(mail+'|'+pw)
    read_acc = '\n'.join(read_acc)
    write_acc = open('fullacc.txt','w',encoding='utf-8')
    write_acc.write(read_acc)
    write_acc.close()



    read_acc = open('mail.txt','r',encoding='utf-8').read().splitlines()
    read_acc = read_acc[1:]
    read_acc = '\n'.join(read_acc)
    write_acc = open('mail.txt','w',encoding='utf-8')
    write_acc.write(read_acc)
    write_acc.close()


    driver.find_element_by_id('paypalAccountData_emailPassword').click()
    time.sleep(random.randint(1,3))




    
    driver.find_element_by_id('paypalAccountData_dob').send_keys(str(random.randint(1,2)))
    time.sleep(1)
    driver.find_element_by_id('paypalAccountData_dob').send_keys(str(random.randint(1,8)))
    time.sleep(1)
    driver.find_element_by_id('paypalAccountData_dob').send_keys('0')
    time.sleep(1)
    driver.find_element_by_id('paypalAccountData_dob').send_keys(str(random.randint(1,9)))
    time.sleep(1)
    driver.find_element_by_id('paypalAccountData_dob').send_keys('1')
    time.sleep(1)
    driver.find_element_by_id('paypalAccountData_dob').send_keys('9')
    time.sleep(1)
    driver.find_element_by_id('paypalAccountData_dob').send_keys(str(random.randint(7,9)))
    time.sleep(1)
    driver.find_element_by_id('paypalAccountData_dob').send_keys(str(random.randint(0,9)))




    driver.find_element_by_id('paypalAccountData_identificationNum').send_keys(str(random.randint(100000,999999))+str(random.randint(100000,999999)))
    driver.find_element_by_id('paypalAccountData_address1_0').send_keys(random.choice(open('data/local','r',encoding='utf-8').read().splitlines()))
    driver.find_element_by_id('paypalAccountData_address2_0').send_keys(random.choice(open('data/local','r',encoding='utf-8').read().splitlines()))
    driver.find_element_by_id('paypalAccountData_city_0').send_keys(random.choice(open('data/local','r',encoding='utf-8').read().splitlines()))
    driver.find_element_by_id('dropdownMenuButton_paypalAccountData_state_0').click()
    time.sleep(random.randint(1,3))
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div/div/form/fieldset/div/div[9]/div[1]/div/div/ul/li['+str(random.randint(1,20))+']').click()
    driver.find_element_by_id('paypalAccountData_zip_0').send_keys(str(random.randint(1,999999)))
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div/div/form/fieldset/div/div[10]/div/div/div/label/span').click()
    time.sleep(random.randint(1,3))
    driver.find_element_by_id('paypalAccountData_emailPassword').click()
    time.sleep(30)
    driver.quit()

