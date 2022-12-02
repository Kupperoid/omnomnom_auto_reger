import requests
from bs4 import BeautifulSoup
from proxy_info import login, password
import time
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

proxies = {
    'https': f'http://{login}:{password}@proxy.site:11111'
}

url_omnom = 'https://api.truefuture.io/contact-us/subscription'

def main():
    f = open('mail.txt', 'r')
    for i in f:
        user_agent = user_agent_rotator.get_random_user_agent()
        headers = {
            'User-Agent': user_agent
        }
        r = requests.get('') #proxy link for change IP 
        time.sleep(5)
        mail = i.rstrip()
        body_omnom = {
            "address": f"{mail}",
            "project": "om nom"
        }
        om = requests.post(url_omnom, json= body_omnom, headers=headers, proxies=proxies)
        print(f'{om} - {mail} ')
    f.close()

if __name__ == '__main__':
    main()