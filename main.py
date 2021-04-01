from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time, random
from gui import TelaPython

tela = TelaPython()
a = tela.iniciar()
b = f'{a}'
c = b.replace(" ", "+")

#Random Proxy
proxy = set()

with open("proxys.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy.add(line1.strip())

PROXY = random.choice(list(proxy))
#PROXY = '204.101.61.82:4145'
print(PROXY)
#Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server=http://{PROXY}')
chrome_options.add_argument('--user-agent=')
chrome = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
chrome.get(f"https://www.ean-search.org/?q={c}")


